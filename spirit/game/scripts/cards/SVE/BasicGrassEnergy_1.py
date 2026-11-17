from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="8a9eba81-b73f-57f5-ad14-e8e8549dbda1",
    key="SVE",
    name="Basic Grass Energy",
    display_name="Basic Grass Energy",
    searchable_by=["Basic Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.GRASS,
    is_special=False
)
