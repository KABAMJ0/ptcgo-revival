from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="49f97d33-3933-589d-be61-716debd02a54",
    key="SVE",
    name="Basic Fighting Energy",
    display_name="Basic Fighting Energy",
    searchable_by=["Basic Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False
)
