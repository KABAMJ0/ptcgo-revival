from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ea127f2b-ba52-5d4e-b795-d8bb3663e310",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latiasex.Name",
    display_name="Latias ex",
    searchable_by=["Latias ex", "Basic", "ex", "Latiasex"],
    subtypes=["Basic", "ex"],
    collector_number=93,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=380,
    abilities=[
        Attack(
            title="Hypnoblast",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Mist Ball",
            game_text="Discard a Fire Energy and a Water Energy attached to Latias ex.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)