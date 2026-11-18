from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="813dd652-74ad-5d69-9f3c-04f131aec2b2",
    key="SVE",
    name="Basic Psychic Energy",
    display_name="Basic Psychic Energy",
    searchable_by=["Basic Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SVE",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False
)
