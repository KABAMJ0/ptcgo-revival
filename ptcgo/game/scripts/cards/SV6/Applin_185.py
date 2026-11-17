from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d28986bd-9490-53d8-bc8e-9737b3571ce3",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    display_name="Applin",
    searchable_by=["Applin", "Basic", "Applin"],
    subtypes=["Basic"],
    collector_number=185,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=840,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=30,
        ),
    ],
)