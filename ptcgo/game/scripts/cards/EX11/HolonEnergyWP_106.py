from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="923b0a11-4523-56dd-a11c-9b696c81042b",
    key="EX11",
    name="Holon Energy WP",
    display_name="Holon Energy WP",
    searchable_by=["Holon Energy WP", "Special"],
    subtypes=["Special"],
    collector_number=106,
    set_code="EX11",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
