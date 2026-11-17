from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="e102d84e-7447-5283-b2b4-db32af71a0c1",
    key="XY10",
    name="Strong Energy",
    display_name="Strong Energy",
    searchable_by=["Strong Energy", "Special"],
    subtypes=["Special"],
    collector_number=115,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
