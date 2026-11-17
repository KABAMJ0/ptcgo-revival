from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d96d9554-e503-54c6-9790-369e91621fb1",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSamurottV.Name",
    display_name="Hisuian Samurott V",
    searchable_by=["Hisuian Samurott V", "Basic", "V", "HisuianSamurottV"],
    subtypes=["Basic", "V"],
    collector_number=51,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=503,
    abilities=[
        Attack(
            title="Basket Crash",
            game_text="Discard up to 2 Pok\u00e9mon Tools from your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Slash",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=180,
            effect=unimplemented,
        ),
    ],
)