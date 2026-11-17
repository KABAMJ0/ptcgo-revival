from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d5d4bb36-5bcd-50cd-be33-68d42d985b2f",
    key="ME4",
    name="Bubbly Water Energy",
    display_name="Bubbly Water Energy",
    searchable_by=["Bubbly Water Energy", "Special"],
    subtypes=["Special"],
    collector_number=84,
    set_code="ME4",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
