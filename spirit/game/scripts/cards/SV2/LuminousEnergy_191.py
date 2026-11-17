from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="110114bd-d1cb-5149-afe8-4a1e1b002786",
    key="SV2",
    name="Luminous Energy",
    display_name="Luminous Energy",
    searchable_by=["Luminous Energy", "Special"],
    subtypes=["Special"],
    collector_number=191,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
