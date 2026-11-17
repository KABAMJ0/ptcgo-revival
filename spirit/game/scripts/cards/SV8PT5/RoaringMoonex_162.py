from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6599c675-fa54-531d-afbf-1d4585a72c9d",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RoaringMoonex.Name",
    display_name="Roaring Moon ex",
    searchable_by=["Roaring Moon ex", "Basic", "ex", "Ancient", "RoaringMoonex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=162,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    abilities=[
        Attack(
            title="Frenzied Gouging",
            game_text="Knock Out your opponent's Active Pok\u00e9mon. If your opponent's Active Pok\u00e9mon is Knocked Out in this way, this Pok\u00e9mon does 200 damage to itself.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Calamity Storm",
            game_text="You may discard a Stadium in play. If you do, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)