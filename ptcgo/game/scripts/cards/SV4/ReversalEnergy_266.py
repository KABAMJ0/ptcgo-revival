from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f39253d2-1bd7-5964-8f48-a643d2761905",
    key="SV4",
    name="Reversal Energy",
    display_name="Reversal Energy",
    searchable_by=["Reversal Energy", "Special"],
    subtypes=["Special"],
    collector_number=266,
    set_code="SV4",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
