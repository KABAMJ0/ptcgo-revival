from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4dadbf5e-2885-5f61-9171-e2d5f2cd67d3",
    key="SVE",
    name="Basic Water Energy",
    display_name="Basic Water Energy",
    searchable_by=["Basic Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.WATER,
    is_special=False
)
