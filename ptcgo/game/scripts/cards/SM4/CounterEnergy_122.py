from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="78aeabfd-1bd4-575a-960d-031180c8cd49",
    key="SM4",
    name="Counter Energy",
    display_name="Counter Energy",
    searchable_by=["Counter Energy", "Special"],
    subtypes=["Special"],
    collector_number=122,
    set_code="SM4",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
