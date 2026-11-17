from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="129741bb-9ee9-51b4-9ab2-2e7bc81035cb",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TangrowthLVX.Name",
    display_name="Tangrowth LV.X",
    searchable_by=["Tangrowth LV.X", "Level-Up", "TangrowthLVX"],
    subtypes=["Level-Up"],
    collector_number=99,
    set_code="PL4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name",
    family_id=114,
    abilities=[
        Ability(
            title="Healing Growth",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, remove 4 damage counters from 1 of your Pok\u00e9mon. This power can't be used if Tangrowth is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Big Growth",
            game_text="Search your discard pile for as many Grass Energy cards as you like and attach them to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
    ],
)