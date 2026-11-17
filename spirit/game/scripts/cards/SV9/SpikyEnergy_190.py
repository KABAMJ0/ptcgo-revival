from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f9881aa9-4f57-582e-bcb2-77c433a250ad",
    key="SV9",
    name="Spiky Energy",
    display_name="Spiky Energy",
    searchable_by=["Spiky Energy", "Special"],
    subtypes=["Special"],
    collector_number=190,
    set_code="SV9",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
