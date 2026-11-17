from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="293cc6c2-2a0a-50fa-8a57-1853ebd5d9d1",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latiosex.Name",
    display_name="Latios ex δ",
    searchable_by=["Latios ex \u03b4", "Basic", "ex", "Latiosex"],
    subtypes=["Basic", "ex"],
    collector_number=96,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=381,
    abilities=[
        Ability(
            title="Link Wing",
            game_text="The Retreat Cost for each of your Latias, Latias ex, Latios, and Latios ex is 0.",
            effect=unimplemented,
        ),
        Attack(
            title="Ice Barrier",
            game_text="Prevent all effects of attack, including damage, done to Latios ex by your opponent's Pok\u00e9mon-ex during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)