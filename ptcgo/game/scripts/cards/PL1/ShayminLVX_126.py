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

from ptcgo.game.card_effects.passives_common import team_hp_bonus, pokemon_of_types
from ptcgo.game.attributes import PokemonTypes


GRASS = pokemon_of_types(PokemonTypes.GRASS)


def _grass_team(pokemon, carrier) -> bool:
    """Your Grass Pokemon, excluding Shaymin itself."""
    if pokemon is None or carrier is None:
        return False
    if pokemon.owning_player_id != getattr(carrier, "owning_player_id", None):
        return False
    if "Shaymin" in (getattr(def_for(pokemon.archetype_id), "display_name", "") or ""):
        return False
    return GRASS(pokemon)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="abaa5283-2398-5e01-afb4-917f5892834b",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminLVX.Name",
    display_name="Shaymin LV.X",
    searchable_by=["Shaymin LV.X", "Level-Up", "ShayminLVX"],
    subtypes=["Level-Up"],
    collector_number=126,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    family_id=492,
    abilities=[
        Ability(
            title="Thankfulness",
            game_text="Each of your Grass Pok\u00e9mon (excluding any Shaymin) gets +40 HP. You can't use more than 1 Thankfulness Pok\u00e9-Body each turn.",
            passive=team_hp_bonus(40, protects="team", pred=_grass_team,
                                  stacking_key="Thankfulness"),
        ),
        Attack(
            title="Seed Flare",
            game_text="Choose as many Grass Energy cards from your hand as you like and attach them to your Pok\u00e9mon in any way you like. If you do, this attack does 40 damage plus 20 more damage for each Grass Energy attached in this way.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)