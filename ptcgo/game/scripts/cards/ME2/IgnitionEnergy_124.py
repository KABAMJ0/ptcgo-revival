from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5491db34-56f7-511f-a6e6-6c259c377820",
    key="ME2",
    name="Ignition Energy",
    display_name="Ignition Energy",
    searchable_by=["Ignition Energy", "Special"],
    subtypes=["Special"],
    collector_number=124,
    set_code="ME2",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
