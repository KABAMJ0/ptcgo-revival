from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9f4cf21-e9c2-5028-aab5-8289c66561b5",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsArticunoex.Name",
    display_name="Rocket's Articuno ex",
    searchable_by=["Rocket's Articuno ex", "Basic", "ex", "RocketsArticunoex"],
    subtypes=["Basic", "ex"],
    collector_number=96,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=144,
    abilities=[
        Ability(
            title="Darkness Veil",
            game_text="As long as Rocket's Articuno ex has any Darkness Energy attached to it, prevent all effects, except damage, by an opponent's attack done to Rocket's Articuno ex.",
            effect=unimplemented,
        ),
        Attack(
            title="Freeze Solid",
            game_text="Search your discard pile for a Water Energy card and attach it to Rocket's Articuno ex.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Ice Wing",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)