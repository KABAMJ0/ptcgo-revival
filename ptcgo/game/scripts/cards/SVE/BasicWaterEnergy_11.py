from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="7a51d332-f1f3-5c4a-bddf-b1c19f449f4b",
    key="SVE",
    name="Basic Water Energy",
    display_name="Basic Water Energy",
    searchable_by=["Basic Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.WATER,
    is_special=False
)
