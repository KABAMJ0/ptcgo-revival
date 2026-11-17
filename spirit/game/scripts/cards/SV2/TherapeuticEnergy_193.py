from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="748f89bd-79fe-52cc-b070-6e6441e4ece0",
    key="SV2",
    name="Therapeutic Energy",
    display_name="Therapeutic Energy",
    searchable_by=["Therapeutic Energy", "Special"],
    subtypes=["Special"],
    collector_number=193,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
