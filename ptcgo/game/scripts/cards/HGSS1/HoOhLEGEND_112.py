from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import rewrite_energy_types_passive

card = PokemonCardDef(
    guid="b1b5672d-cf9f-5443-928c-1701756ffffc",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhLEGEND.Name",
    display_name="Ho-Oh LEGEND",
    searchable_by=["Ho-Oh LEGEND", "LEGEND", "HoOhLEGEND"],
    subtypes=["LEGEND"],
    collector_number=112,
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
            passive=rewrite_energy_types_passive(PokemonTypes.FIRE.value),
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