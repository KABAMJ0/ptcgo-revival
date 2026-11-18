from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="436e6ceb-6880-56c0-9603-e6d61087579a",
    key="RSV10PT5",
    name="Ignition Energy",
    display_name="Ignition Energy",
    searchable_by=["Ignition Energy", "Special"],
    subtypes=["Special"],
    collector_number=86,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
