from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="8a514abf-635f-54a3-83ec-7f0ef5585be4",
    key="EX9",
    name="Multi Energy",
    display_name="Multi Energy",
    searchable_by=["Multi Energy", "Special"],
    subtypes=["Special"],
    collector_number=89,
    set_code="EX9",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
