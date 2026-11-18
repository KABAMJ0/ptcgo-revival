from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="b7240297-72ff-53ce-be7b-66c217daca3f",
    key="XY8",
    name="Burning Energy",
    display_name="Burning Energy",
    searchable_by=["Burning Energy", "Special"],
    subtypes=["Special"],
    collector_number=151,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
