from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="6cbae976-e5da-5237-b1f5-31353e67a75e",
    key="SV2",
    name="Basic Water Energy",
    display_name="Basic Water Energy",
    searchable_by=["Basic Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=279,
    set_code="SV2",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.WATER,
    is_special=False
)
