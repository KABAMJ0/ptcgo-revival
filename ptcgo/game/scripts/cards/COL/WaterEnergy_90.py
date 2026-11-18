from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="35a98550-08c8-5579-9555-6f00ae25d8d3",
    key="COL",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="COL",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.WATER,
    is_special=False
)
