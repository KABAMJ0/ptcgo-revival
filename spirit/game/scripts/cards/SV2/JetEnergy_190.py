from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c54a2bd2-ab33-5b3a-9643-c7f02554b640",
    key="SV2",
    name="Jet Energy",
    display_name="Jet Energy",
    searchable_by=["Jet Energy", "Special"],
    subtypes=["Special"],
    collector_number=190,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
