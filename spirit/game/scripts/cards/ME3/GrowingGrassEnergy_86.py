from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="39fcae45-df12-57cd-8d69-4403cf91279d",
    key="ME3",
    name="Growing Grass Energy",
    display_name="Growing Grass Energy",
    searchable_by=["Growing Grass Energy", "Special"],
    subtypes=["Special"],
    collector_number=86,
    set_code="ME3",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
