from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.card_effects.attacks_common import damage_per, damage_counters_on
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import is_pokemon_ex
from ptcgo.game.session.passives import Passive, carrier_pokemon


class FragileHuskPassive(Passive):
    """Knocked Out by an opponent's Pokemon ex attack: no Prize cards."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return count
        if not ctx.is_attack_effect():
            return count
        attacker = getattr(ctx, "attacker", None)
        if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
            return count
        if not is_pokemon_ex(attacker):
            return count
        return 0


card = PokemonCardDef(
    guid="762bf41f-7a8e-5c31-9435-ef5eeaa187bd",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1", "Shedinja"],
    subtypes=["Stage 1"],
    collector_number=144,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Fragile Husk",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon ex, your opponent can't take any Prize cards for it.",
            passive=FragileHuskPassive(),
        ),
        Attack(
            title="Damage Beat",
            game_text="This attack does 20 damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(damage_counters_on('defender'), 20),
        ),
    ],
)