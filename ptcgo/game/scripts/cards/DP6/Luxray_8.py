from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import subtypes_for
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.pokemon import is_lightning_energy
from ptcgo.game.card_effects.passives_common import Passive, carrier_pokemon
from ptcgo.game.card_effects.support_common import attach_from_discard


def _is_level_up(pokemon):
    return "Level-Up" in (subtypes_for(pokemon.archetype_id) or [])


class _Rivalry(Passive):
    """+50 to Luxray's attacks on the Active while the opponent has a LV.X."""

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if not (calc.is_attack and calc.is_opposing and attacker is not None):
            return
        if carrier_pokemon(carrier) is not attacker or not calc.to_active:
            return
        owner = attacker.owning_player_id
        for player_id in calc.board.player_ids:
            if player_id == owner:
                continue
            if any(_is_level_up(pokemon) for pokemon in calc.board.pokemon_in_play(player_id)):
                calc.amount += 50
                return


card = PokemonCardDef(
    guid="a63384ed-5e61-5191-a276-f2683beaf653",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2", "Luxray"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Ability(
            title="Rivalry",
            game_text="If your opponent has any Pok\u00e9mon LV.X in play, each of Luxray's attacks does 50 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=_Rivalry(),
        ),
        Attack(
            title="Plasma",
            game_text="Search your discard pile for a Lightning Energy card and attach it to Luxray.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=attach_from_discard(predicate=is_lightning_energy, count=1, target="self"),
        ),
        Attack(
            title="Shock Bolt",
            game_text="Discard all Lightning Energy attached to Luxray.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=self_energy_discard_attack(all_energy=True, energy_type=PokemonTypes.LIGHTNING),
        ),
    ],
)