from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="cf3d6a67-253e-5727-b284-ce8ba6540fb8",
    key="TATM",
    name="Double Magma Energy",
    display_name="Double Magma Energy",
    searchable_by=["Double Magma Energy", "Special"],
    subtypes=["Special"],
    collector_number=34,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
