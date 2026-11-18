from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="ed1ae23e-df29-52ec-8303-76ce2738e1d2",
    key="DP7",
    name="Cyclone Energy",
    display_name="Cyclone Energy",
    searchable_by=["Cyclone Energy", "Special"],
    subtypes=["Special"],
    collector_number=94,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
