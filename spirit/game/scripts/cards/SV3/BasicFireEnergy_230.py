from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="2021297c-c80e-5ae3-bb3e-d1a9f207b31d",
    key="SV3",
    name="Basic Fire Energy",
    display_name="Basic Fire Energy",
    searchable_by=["Basic Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=230,
    set_code="SV3",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.FIRE,
    is_special=False
)
