from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c32030c8-9230-59a2-a2be-3bcbde568028",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza δ",
    searchable_by=["Rayquaza \u03b4", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER, PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.WATER,
    family_id=384,
    abilities=[
        Ability(
            title="Hydro Barrier",
            game_text="As long as Rayquaza has any Holon Energy cards attached to it, each of your Water Pok\u00e9mon has no Weakness.",
            effect=unimplemented,
        ),
        Attack(
            title="Delta Search",
            game_text="Search your deck for a Holon Energy card and attach it to Rayquaza. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Ozone Flare",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)