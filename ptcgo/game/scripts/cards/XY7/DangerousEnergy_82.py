from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="78e5fa25-878f-55e7-bcd4-b3384e0143aa",
    key="XY7",
    name="Dangerous Energy",
    display_name="Dangerous Energy",
    searchable_by=["Dangerous Energy", "Special"],
    subtypes=["Special"],
    collector_number=82,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
