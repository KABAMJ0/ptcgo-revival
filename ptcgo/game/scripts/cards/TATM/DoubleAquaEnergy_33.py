from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="483ce702-6169-5dbe-9e8d-8f08a8a1bf52",
    key="TATM",
    name="Double Aqua Energy",
    display_name="Double Aqua Energy",
    searchable_by=["Double Aqua Energy", "Special"],
    subtypes=["Special"],
    collector_number=33,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
