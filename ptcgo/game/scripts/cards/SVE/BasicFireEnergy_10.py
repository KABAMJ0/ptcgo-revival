from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="bee9ad80-46e6-5292-8881-42931f1d3fcb",
    key="SVE",
    name="Basic Fire Energy",
    display_name="Basic Fire Energy",
    searchable_by=["Basic Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIRE,
    is_special=False
)
