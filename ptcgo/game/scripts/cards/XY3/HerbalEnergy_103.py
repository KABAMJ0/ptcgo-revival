from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="bfab5dfb-d17a-5dd9-86df-ab0632aebafe",
    key="XY3",
    name="Herbal Energy",
    display_name="Herbal Energy",
    searchable_by=["Herbal Energy", "Special"],
    subtypes=["Special"],
    collector_number=103,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
