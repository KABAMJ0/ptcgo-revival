from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="de23ef8b-9165-5340-87f7-3837ce1bc02f",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Attack(
            title="Chilling Sigh",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Tri Edge",
            game_text="Flip 3 coins. This attack does 40 more damage for each heads.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)