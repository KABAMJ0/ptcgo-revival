from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d23c26b2-8e5c-558d-9078-6329162bc497",
    key="SV6",
    name="Luminous Energy",
    display_name="Luminous Energy",
    searchable_by=["Luminous Energy", "Special"],
    subtypes=["Special"],
    collector_number=226,
    set_code="SV6",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
