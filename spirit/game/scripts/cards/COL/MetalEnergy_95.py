from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="03949fc1-1272-569c-a437-47504abb96d8",
    key="COL",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="COL",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.METAL,
    is_special=False
)
