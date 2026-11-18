from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae2de566-2c90-57dd-9ce0-b107cd156e32",
    key="MCD12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    display_name="Pignite",
    searchable_by=["Pignite", "Stage 1", "Pignite"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="MCD12",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name",
    family_id=499,
    abilities=[
        Attack(
            title="Flame Charge",
            game_text="Search your deck for a Fire Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Heat Crash",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)