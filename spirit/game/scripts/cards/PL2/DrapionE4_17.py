from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dedf4838-e012-5abb-a8db-6ab569c24c54",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrapionE4.Name",
    display_name="Drapion E4",
    searchable_by=["Drapion E4", "Basic", "SP", "DrapionE4"],
    subtypes=["Basic", "SP"],
    collector_number=17,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=452,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Mega Impact",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)