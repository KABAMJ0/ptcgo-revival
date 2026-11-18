from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="ad33f68c-d32f-5a5c-a25d-b02887a37b9e",
    key="HGSS1",
    name="Lightning Energy",
    display_name="Lightning Energy",
    searchable_by=["Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="HGSS1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False
)
