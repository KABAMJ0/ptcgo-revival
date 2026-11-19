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

from ptcgo.game.card_effects.passives_common import prevent_damage_when


def _from_kind_holder(calc, carrier) -> bool:
    """Prevent everything from an attacker holding a Power or Body."""
    attacker = calc.attacker
    return _has_kind(attacker, AbilityTypes.POKE_POWER,
                     AbilityTypes.POKE_BODY)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="787794c8-9f95-5636-b8ff-dbf90114f343",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1", "Shedinja"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Marvel Shell",
            game_text="Prevent all effects of attacks, including damage, done to Shedinja by your opponent's Pok\u00e9mon that has any Pok\u00e9-Powers or Pok\u00e9-Bodies.",
            passive=prevent_damage_when(_from_kind_holder),
        ),
        Attack(
            title="Spike Wound",
            game_text="Choose 1 of your opponent's Pok\u00e9mon that has any damage counters on it. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)