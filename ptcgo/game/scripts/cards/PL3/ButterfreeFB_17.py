from ptcgo.game.attributes import AbilityTypes
from ptcgo.game.data_utils import def_for


def _has_kind(pokemon, *kinds):
    """Whether this Pokemon carries a printed ability of one of `kinds`
    (POKE_POWER / POKE_BODY), read off the definition's restored kinds."""
    if pokemon is None:
        return False
    definition = def_for(pokemon.archetype_id)
    for ability in getattr(definition, "abilities", []) or []:
        if getattr(ability, "ability_type", None) in kinds:
            return True
    return False

from ptcgo.game.card_effects.passives_common import typed_damage_boost_tool


def _defender_has_body(target) -> bool:
    return _has_kind(target, AbilityTypes.POKE_BODY)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2a09df1a-8daf-50d2-948c-417d17064e3e",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ButterfreeFB.Name",
    display_name="Butterfree FB",
    searchable_by=["Butterfree FB", "Basic", "SP", "ButterfreeFB"],
    subtypes=["Basic", "SP"],
    collector_number=17,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=12,
    abilities=[
        Ability(
            title="Compound Eyes",
            game_text="If your opponent's Active Pok\u00e9mon has any Pok\u00e9-Bodies, each of Butterfree FB's attacks does 30 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=typed_damage_boost_tool(_defender_has_body, 30),
        ),
        Attack(
            title="Select Powder",
            game_text="Choose either Burned or Poisoned. The Defending Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)