from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="118013fc-9de9-5215-bd40-6bfd7e48e008",
    key="EX7",
    name="R Energy",
    display_name="R Energy",
    searchable_by=["R Energy", "Special"],
    subtypes=["Special"],
    collector_number=95,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
