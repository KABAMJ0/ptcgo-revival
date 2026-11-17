from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d9c8bc79-bede-562b-9e9f-e31ee5d8979e",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name",
    display_name="Magby",
    searchable_by=["Magby", "Basic", "Magby"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="HGSS4",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=240,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Magby is Asleep, prevents all damage done to Magby by attacks.",
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