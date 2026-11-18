from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ba757d91-47f5-54aa-8bd4-66a7730fb080",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic", "Xerneas"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=716,
    abilities=[
        Attack(
            title="Geo Gate",
            game_text="Search your deck for up to 3 Basic Psychic Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Bright Horns",
            game_text="During your next turn, this Pok\u00e9mon can't use Bright Horns.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)