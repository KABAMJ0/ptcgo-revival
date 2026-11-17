from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7864301e-05ba-5913-8eae-8905a354af04",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GougingFireex.Name",
    display_name="Gouging Fire ex",
    searchable_by=["Gouging Fire ex", "Basic", "ex", "Ancient", "GougingFireex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=144,
    set_code="SVP",
    rarity=Rarities.RarePromo,
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