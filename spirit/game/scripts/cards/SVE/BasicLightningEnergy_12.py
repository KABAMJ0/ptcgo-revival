from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="64708b6e-f73a-5dcd-804e-3d3aee062d03",
    key="SVE",
    name="Basic Lightning Energy",
    display_name="Basic Lightning Energy",
    searchable_by=["Basic Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False
)
