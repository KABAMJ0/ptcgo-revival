from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="ad1a7ee4-285b-539f-8a50-c264a88bb858",
    key="NEO1",
    name="Recycle Energy",
    display_name="Recycle Energy",
    searchable_by=["Recycle Energy", "Special"],
    subtypes=["Special"],
    collector_number=105,
    set_code="NEO1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
