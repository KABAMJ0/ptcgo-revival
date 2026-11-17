from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="76a9c1e5-de7a-5b7d-8231-3d5752c9bf5d",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CentiskorchV.Name",
    display_name="Centiskorch V",
    searchable_by=["Centiskorch V", "Basic", "V", "CentiskorchV"],
    subtypes=["Basic", "V"],
    collector_number=108,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=851,
    abilities=[
        Attack(
            title="Radiating Heat",
            game_text="You may discard an Energy from this Pok\u00e9mon. If you do, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Burning Train",
            cost={PokemonTypes.FIRE: 4},
            damage=180,
        ),
    ],
)