from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e9f4efd7-ae96-5796-b74e-7d02767e9296",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenneex.Name",
    display_name="Dedenne ex",
    searchable_by=["Dedenne ex", "Basic", "Tera", "ex", "Dedenneex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=93,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=702,
    abilities=[
        Attack(
            title="Tail Swap",
            game_text="Move all damage counters from 1 of your Benched Pok\u00e9mon to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Wondrous Shot",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=170,
            effect=unimplemented,
        ),
    ],
)