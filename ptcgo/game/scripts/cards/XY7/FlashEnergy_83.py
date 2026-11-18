from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import pokemon_of_type
card = EnergyCardDef(
    guid="695127e4-2bf0-5ceb-855f-ed7aea962aa0",
    key="XY7",
    name="Flash Energy",
    display_name="Flash Energy",
    searchable_by=["Flash Energy", "Special"],
    subtypes=["Special"],
    collector_number=83,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=pokemon_of_type(PokemonTypes.LIGHTNING),
)
