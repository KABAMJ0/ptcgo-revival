from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4d906f0c-fb41-5857-b0c9-07d6e2dc3e71",
    key="ME5",
    name="Voltaic Lightning Energy",
    display_name="Voltaic Lightning Energy",
    searchable_by=["Voltaic Lightning Energy", "Special"],
    subtypes=["Special"],
    collector_number=84,
    set_code="ME5",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
