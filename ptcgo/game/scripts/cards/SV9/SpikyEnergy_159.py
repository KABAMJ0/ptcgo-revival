from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="a1609c13-6330-50b6-9d7a-1cf85f78fe70",
    key="SV9",
    name="Spiky Energy",
    display_name="Spiky Energy",
    searchable_by=["Spiky Energy", "Special"],
    subtypes=["Special"],
    collector_number=159,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
