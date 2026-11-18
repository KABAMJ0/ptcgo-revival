from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import pokemon_with_subtype, ALL_TYPES_ONE_AT_A_TIME
card = EnergyCardDef(
    guid="4e7a1516-dba1-584a-9479-a0f41bc58742",
    key="SWSH6",
    name="Impact Energy",
    display_name="Impact Energy",
    searchable_by=["Impact Energy", "Special", "Single Strike"],
    subtypes=["Special", "Single Strike"],
    collector_number=157,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=pokemon_with_subtype("Single Strike"),
    provides=ALL_TYPES_ONE_AT_A_TIME,
)
