from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="95271e08-2bcc-522a-853a-3c918b94c12f",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IceRiderCalyrexV.Name",
    display_name="Ice Rider Calyrex V",
    searchable_by=["Ice Rider Calyrex V", "Basic", "V", "IceRiderCalyrexV"],
    subtypes=["Basic", "V"],
    collector_number=14,
    set_code="SWSH10TG",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=898,
    abilities=[
        Attack(
            title="Pierce",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
        Attack(
            title="Glacial Lance",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)