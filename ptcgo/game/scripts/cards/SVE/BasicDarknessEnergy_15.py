from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c47f51b2-8202-5f76-8afd-87e798658373",
    key="SVE",
    name="Basic Darkness Energy",
    display_name="Basic Darkness Energy",
    searchable_by=["Basic Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False
)
