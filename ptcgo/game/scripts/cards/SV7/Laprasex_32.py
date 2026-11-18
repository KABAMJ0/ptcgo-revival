from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2b8928a5-4ae7-5256-b74f-c6404e7d70f5",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Laprasex.Name",
    display_name="Lapras ex",
    searchable_by=["Lapras ex", "Basic", "Tera", "ex", "Laprasex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=32,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=131,
    abilities=[
        Attack(
            title="Power Splash",
            game_text="This attack does 40 damage for each Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Larimar Rain",
            game_text="Look at the top 20 cards of your deck and attach any number of Energy cards you find there to your Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            effect=unimplemented,
        ),
    ],
)