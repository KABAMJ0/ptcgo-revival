from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import pokemon_with_subtype, ALL_TYPES_ONE_AT_A_TIME
card = EnergyCardDef(
    guid="a1be9557-4439-5c31-8c90-51a75824090f",
    key="SWSH8",
    name="Fusion Strike Energy",
    display_name="Fusion Strike Energy",
    searchable_by=["Fusion Strike Energy", "Fusion Strike", "Special"],
    subtypes=["Fusion Strike", "Special"],
    collector_number=244,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=pokemon_with_subtype("Fusion Strike"),
    provides=ALL_TYPES_ONE_AT_A_TIME,
)
