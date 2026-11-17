from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a63cc0e0-45ca-57c4-a2ea-11222158f0a0",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tatsugiriex.Name",
    display_name="Tatsugiri ex",
    searchable_by=["Tatsugiri ex", "Basic", "Tera", "ex", "Tatsugiriex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=226,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=978,
    abilities=[
        Attack(
            title="Surprise Pump",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=100,
            effect=unimplemented,
        ),
        Attack(
            title="Cinnabar Lure",
            game_text="Look at the top 10 cards of your deck. You may put any number of Pok\u00e9mon you find there onto your Bench. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
    ],
)