from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f38f94f4-4cac-5f50-a89d-a4ee092fcaff",
    key="SVE",
    name="Basic Psychic Energy",
    display_name="Basic Psychic Energy",
    searchable_by=["Basic Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False
)
