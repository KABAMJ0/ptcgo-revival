from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="52f3ad85-6dbb-5bc5-b4c6-795a4d5241a6",
    key="COL",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="COL",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIRE,
    is_special=False
)
