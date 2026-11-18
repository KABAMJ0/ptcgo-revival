from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="afc074ad-64ee-58b9-9a3c-11006d765596",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GrimmsnarlV.Name",
    display_name="Grimmsnarl V",
    searchable_by=["Grimmsnarl V", "Basic", "V", "GrimmsnarlV"],
    subtypes=["Basic", "V"],
    collector_number=116,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=861,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title="Spiky Knuckle",
            game_text="Put 2 Darkness Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=200,
            effect=unimplemented,
        ),
    ],
)