from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4cf01ea3-3c35-58db-8613-f16494a66282",
    key="SVE",
    name="Basic Metal Energy",
    display_name="Basic Metal Energy",
    searchable_by=["Basic Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.METAL,
    is_special=False
)
