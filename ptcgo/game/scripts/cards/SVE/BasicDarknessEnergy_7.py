from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d55adb5d-56e2-551f-84f0-ae523e302ac4",
    key="SVE",
    name="Basic Darkness Energy",
    display_name="Basic Darkness Energy",
    searchable_by=["Basic Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False
)
