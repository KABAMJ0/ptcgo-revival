from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fdfc6f21-2dcf-5693-b30d-01f6823366d8",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsMoltresex.Name",
    display_name="Rocket's Moltres ex",
    searchable_by=["Rocket's Moltres ex", "Basic", "ex", "RocketsMoltresex"],
    subtypes=["Basic", "ex"],
    collector_number=100,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=146,
    abilities=[
        Ability(
            title="Dark Lift",
            game_text="If Rocket's Moltres ex has any Darkness Energy attached to it, the Retreat Cost for Rocket's Moltres ex is 0.",
            effect=unimplemented,
        ),
        Attack(
            title="Fire Dance",
            game_text="Search your discard pile for a Fire Energy card and attach it to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)