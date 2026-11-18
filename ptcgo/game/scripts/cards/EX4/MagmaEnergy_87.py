from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d39dd7f6-5354-535d-9c96-836c92be088a",
    key="EX4",
    name="Magma Energy",
    display_name="Magma Energy",
    searchable_by=["Magma Energy", "Special"],
    subtypes=["Special"],
    collector_number=87,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
