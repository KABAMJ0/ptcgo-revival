from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="7ff27a3a-16fa-5261-913d-0fe48af081cd",
    key="BASE5",
    name="Rainbow Energy",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=17,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
