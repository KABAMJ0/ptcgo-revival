from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="88b01fb8-c869-5745-9ce6-1d83c2a8eb53",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowkingex.Name",
    display_name="Slowking ex",
    searchable_by=["Slowking ex", "Stage 1", "Tera", "ex", "Slowkingex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=238,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Profound Knowledge",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Wise Headbutt",
            game_text="You may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            effect=unimplemented,
        ),
    ],
)