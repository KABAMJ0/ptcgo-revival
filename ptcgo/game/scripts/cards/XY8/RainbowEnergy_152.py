from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME, rainbow_on_attach
card = EnergyCardDef(
    guid="00b40821-ca09-5786-a58f-38a549f8bdf6",
    key="XY8",
    name="Rainbow Energy",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=152,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    on_attach=rainbow_on_attach,
)
