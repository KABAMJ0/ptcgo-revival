from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d028a5c3-c094-5925-9374-85e7e25a44f3",
    key="ME5",
    name="Shadowy Darkness Energy",
    display_name="Shadowy Darkness Energy",
    searchable_by=["Shadowy Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=83,
    set_code="ME5",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
