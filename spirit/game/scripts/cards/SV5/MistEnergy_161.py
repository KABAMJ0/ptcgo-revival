from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="545f240a-204f-5cf5-a275-57303c7e88bd",
    key="SV5",
    name="Mist Energy",
    display_name="Mist Energy",
    searchable_by=["Mist Energy", "Special"],
    subtypes=["Special"],
    collector_number=161,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
