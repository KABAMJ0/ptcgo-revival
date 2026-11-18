from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="69def66f-8b0b-5255-84ac-334cde669a32",
    key="XY5",
    name="Shield Energy",
    display_name="Shield Energy",
    searchable_by=["Shield Energy", "Special"],
    subtypes=["Special"],
    collector_number=143,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
