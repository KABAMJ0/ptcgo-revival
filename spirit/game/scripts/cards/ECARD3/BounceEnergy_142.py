from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="211abfd4-15dd-55e5-a362-46f2c7f70ac8",
    key="ECARD3",
    name="Bounce Energy",
    display_name="Bounce Energy",
    searchable_by=["Bounce Energy", "Special"],
    subtypes=["Special"],
    collector_number=142,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
