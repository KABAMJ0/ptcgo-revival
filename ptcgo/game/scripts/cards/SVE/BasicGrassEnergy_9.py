from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="044f3dbc-ce0f-5d48-863c-fc06caa806f4",
    key="SVE",
    name="Basic Grass Energy",
    display_name="Basic Grass Energy",
    searchable_by=["Basic Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.GRASS,
    is_special=False
)
