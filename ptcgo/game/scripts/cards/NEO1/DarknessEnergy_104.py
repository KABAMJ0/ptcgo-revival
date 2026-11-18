from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="b12d049a-5483-58fb-ab91-baefc225e9b7",
    key="NEO1",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=104,
    set_code="NEO1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
