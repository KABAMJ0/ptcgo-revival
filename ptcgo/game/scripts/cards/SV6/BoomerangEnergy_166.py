from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d199da70-33cd-540f-84b6-8ccb3d8bab54",
    key="SV6",
    name="Boomerang Energy",
    display_name="Boomerang Energy",
    searchable_by=["Boomerang Energy", "Special"],
    subtypes=["Special"],
    collector_number=166,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
