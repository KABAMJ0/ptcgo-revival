from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="092ebd97-9c79-50a2-a42f-22e5685c6ddb",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenneex.Name",
    display_name="Dedenne ex",
    searchable_by=["Dedenne ex", "Basic", "Tera", "ex", "Dedenneex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=239,
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