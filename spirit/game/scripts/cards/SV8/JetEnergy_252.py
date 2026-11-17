from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="fda183f0-978f-5211-aa20-d3d59fdd998d",
    key="SV8",
    name="Jet Energy",
    display_name="Jet Energy",
    searchable_by=["Jet Energy", "Special"],
    subtypes=["Special"],
    collector_number=252,
    set_code="SV8",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
