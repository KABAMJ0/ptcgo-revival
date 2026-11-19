from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import attack_effect_shield_passive
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.models.board import BoardState

def _metal_energy_holder(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    return any(energy_provides_type(e, PokemonTypes.METAL.value)
               for e in BoardState.attached_energies(target))


card = PokemonCardDef(
    guid="7bafe9c7-eb6c-5b9a-a750-993feaa785f7",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagearnaEX.Name",
    display_name="Magearna-EX",
    searchable_by=["Magearna-EX", "Basic", "EX", "MagearnaEX"],
    subtypes=["Basic", "EX"],
    collector_number=175,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=801,
    abilities=[
        Ability(
            title="Mystic Heart",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to each of your Pok\u00e9mon that has any Metal Energy attached to it. (Existing effects are not removed.)",
            passive=attack_effect_shield_passive(_metal_energy_holder),
        ),
        Attack(
            title="Soul Blaster",
            game_text="During your next turn, this Pok\u00e9mon's Soul Blaster attack's base damage is 60.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)