from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME, rainbow_on_attach
card = EnergyCardDef(
    guid="72cfb887-6baf-53ac-8576-27247ab151dc",
    key="ECARD2",
    name="Rainbow Energy",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=144,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    on_attach=rainbow_on_attach,
)
