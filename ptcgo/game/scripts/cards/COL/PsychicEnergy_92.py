from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="356110b2-8ebf-5ced-a2b1-1fbf01479385",
    key="COL",
    name="Psychic Energy",
    display_name="Psychic Energy",
    searchable_by=["Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="COL",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False
)
