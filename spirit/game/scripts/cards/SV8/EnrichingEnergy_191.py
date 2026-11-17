from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c0b69a59-9591-516a-abb5-3d8910b0cc9f",
    key="SV8",
    name="Enriching Energy",
    display_name="Enriching Energy",
    searchable_by=["Enriching Energy", "Special", "ACE SPEC"],
    subtypes=["Special", "ACE SPEC"],
    collector_number=191,
    set_code="SV8",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
