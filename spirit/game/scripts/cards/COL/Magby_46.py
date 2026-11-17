from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5c6bdbb5-7ef6-5861-8758-b4293fd296a0",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name",
    display_name="Magby",
    searchable_by=["Magby", "Basic", "Magby"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="COL",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=240,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Magby is Asleep, prevent all damage done to Magby by attacks.",
            effect=unimplemented,
        ),
        Attack(
            title="Play with Fire",
            game_text="The Defending Pok\u00e9mon is now Burned. Magby is now Asleep.",
            cost={},
            effect=unimplemented,
        ),
    ],
)