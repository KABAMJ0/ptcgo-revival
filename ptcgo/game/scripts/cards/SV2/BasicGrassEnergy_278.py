from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d912b785-01ef-5d13-902d-63b07210e350",
    key="SV2",
    name="Basic Grass Energy",
    display_name="Basic Grass Energy",
    searchable_by=["Basic Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=278,
    set_code="SV2",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.GRASS,
    is_special=False
)
