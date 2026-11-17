from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aabab8dc-72c5-577e-8758-6a96867942ff",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GougingFireex.Name",
    display_name="Gouging Fire ex",
    searchable_by=["Gouging Fire ex", "Basic", "ex", "Ancient", "GougingFireex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=188,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
        Attack(
            title="Blaze Blitz",
            game_text="This Pok\u00e9mon can't use Blaze Blitz again until it leaves the Active Spot.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=260,
            effect=unimplemented,
        ),
    ],
)