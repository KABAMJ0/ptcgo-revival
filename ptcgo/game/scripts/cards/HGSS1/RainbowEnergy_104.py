from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME, rainbow_on_attach
card = EnergyCardDef(
    guid="abfb47e3-f643-5387-bc05-0fb50c181d8f",
    key="HGSS1",
    name="Rainbow Energy",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=104,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    on_attach=rainbow_on_attach,
)
