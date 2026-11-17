from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="18067340-de24-5600-9414-57fe907d07c7",
    key="SM4",
    name="Counter Energy",
    display_name="Counter Energy",
    searchable_by=["Counter Energy", "Special"],
    subtypes=["Special"],
    collector_number=100,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
