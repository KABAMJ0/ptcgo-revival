from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="92bd680f-29e5-5779-93da-2d537967a143",
    key="SVE",
    name="Basic Metal Energy",
    display_name="Basic Metal Energy",
    searchable_by=["Basic Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.METAL,
    is_special=False
)
