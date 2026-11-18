from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="68a8763f-d458-5fbd-afa5-33a5bab8722e",
    key="PL2",
    name="Upper Energy",
    display_name="Upper Energy",
    searchable_by=["Upper Energy", "Special"],
    subtypes=["Special"],
    collector_number=102,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
