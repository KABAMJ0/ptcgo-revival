from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="fb3dbaba-4e13-5115-9605-2052ec1d9f1a",
    key="SVE",
    name="Basic Fire Energy",
    display_name="Basic Fire Energy",
    searchable_by=["Basic Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIRE,
    is_special=False
)
