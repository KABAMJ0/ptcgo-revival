from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="7b8107fd-3152-5d6e-b442-f47dc092b256",
    key="EX1",
    name="Rainbow Energy",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=95,
    set_code="EX1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
