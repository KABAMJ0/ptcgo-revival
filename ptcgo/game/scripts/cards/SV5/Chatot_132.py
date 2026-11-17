from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b067696-3810-59d3-8e65-9963b6cd46f9",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chatot.Name",
    display_name="Chatot",
    searchable_by=["Chatot", "Basic", "Chatot"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=441,
    abilities=[
        Attack(
            title="A Cappella",
            game_text="Search your deck for up to 3 Basic Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)