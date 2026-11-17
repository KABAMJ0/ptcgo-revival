from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="8ee9e2f6-2010-5cd1-b830-f9721f632b60",
    key="NEO4",
    name="Miracle Energy",
    display_name="Miracle Energy",
    searchable_by=["Miracle Energy", "Special"],
    subtypes=["Special"],
    collector_number=16,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
