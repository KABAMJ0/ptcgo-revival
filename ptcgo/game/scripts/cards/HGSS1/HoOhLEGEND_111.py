from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6c2dd2bd-d3ff-59cd-861e-7abefba6bb94",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhLEGEND.Name",
    display_name="Ho-Oh LEGEND",
    searchable_by=["Ho-Oh LEGEND", "LEGEND", "HoOhLEGEND"],
    subtypes=["LEGEND"],
    collector_number=111,
    set_code="HGSS1",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Ability(
            title="Sacred Rainbow",
            game_text="All Energy attached to Ho-Oh LEGEND are Fire Energy instead of their usual type.",
            effect=unimplemented,
        ),
        Attack(
            title="Bright Wing",
            game_text="Discard an Energy attached to Ho-Oh LEGEND.",
            cost={PokemonTypes.FIRE: 4},
            damage=100,
            effect=unimplemented,
        ),
    ],
)