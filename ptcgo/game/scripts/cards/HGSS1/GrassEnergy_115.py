from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="2f5fb781-5f6c-5832-b872-c49f6e486e66",
    key="HGSS1",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=115,
    set_code="HGSS1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.GRASS,
    is_special=False
)
