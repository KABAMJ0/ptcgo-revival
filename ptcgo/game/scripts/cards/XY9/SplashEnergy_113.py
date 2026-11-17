from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c7a9536c-e7b4-5e84-803b-f96379054d56",
    key="XY9",
    name="Splash Energy",
    display_name="Splash Energy",
    searchable_by=["Splash Energy", "Special"],
    subtypes=["Special"],
    collector_number=113,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
