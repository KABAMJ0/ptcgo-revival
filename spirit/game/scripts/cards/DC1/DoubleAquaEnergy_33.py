from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="483ce702-6169-5dbe-9e8d-8f08a8a1bf52",
    key="DC1",
    name="Double Aqua Energy",
    display_name="Double Aqua Energy",
    searchable_by=["Double Aqua Energy", "Special"],
    subtypes=["Special"],
    collector_number=33,
    set_code="DC1",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
