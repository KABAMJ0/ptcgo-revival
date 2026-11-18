from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2ebb12f9-3546-534d-bcbe-b0d7e30097ef",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesCutiefly.Name",
    display_name="Lillie's Cutiefly",
    searchable_by=["Lillie's Cutiefly", "Basic", "LilliesCutiefly"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    family_id=742,
    abilities=[
        Attack(
            title="Hold Still",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)