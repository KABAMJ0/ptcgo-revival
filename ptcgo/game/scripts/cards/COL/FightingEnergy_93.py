from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d0462beb-572f-5b6a-9153-a00c8ba7b821",
    key="COL",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="COL",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False
)
