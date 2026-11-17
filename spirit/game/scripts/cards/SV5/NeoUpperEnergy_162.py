from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="3db38fbe-a4be-5def-bea0-9cf220ae79d4",
    key="SV5",
    name="Neo Upper Energy",
    display_name="Neo Upper Energy",
    searchable_by=["Neo Upper Energy", "Special", "ACE SPEC"],
    subtypes=["Special", "ACE SPEC"],
    collector_number=162,
    set_code="SV5",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
