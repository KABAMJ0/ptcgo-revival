from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="9d2c32d3-8b21-5c68-852e-e501a033cb86",
    key="HGSS1",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="HGSS1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIRE,
    is_special=False
)
