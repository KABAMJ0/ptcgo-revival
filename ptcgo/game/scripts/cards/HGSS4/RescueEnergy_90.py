from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="2309a562-6e8f-550a-9ad2-733b6873e449",
    key="HGSS4",
    name="Rescue Energy",
    display_name="Rescue Energy",
    searchable_by=["Rescue Energy", "Special"],
    subtypes=["Special"],
    collector_number=90,
    set_code="HGSS4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
