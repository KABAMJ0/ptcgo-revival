from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="18e07f45-2ba3-57eb-a0d1-17e0845c4c39",
    key="EX13",
    name="δ Rainbow Energy",
    display_name="δ Rainbow Energy",
    searchable_by=["\u03b4 Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=98,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
