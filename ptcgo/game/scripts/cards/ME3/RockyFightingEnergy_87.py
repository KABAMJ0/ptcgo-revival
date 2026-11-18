from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="611d1f76-0535-5826-bcbc-c62ec7d3a89b",
    key="ME3",
    name="Rocky Fighting Energy",
    display_name="Rocky Fighting Energy",
    searchable_by=["Rocky Fighting Energy", "Special"],
    subtypes=["Special"],
    collector_number=87,
    set_code="ME3",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
