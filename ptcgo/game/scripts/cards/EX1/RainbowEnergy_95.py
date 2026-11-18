from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME, rainbow_on_attach
card = EnergyCardDef(
    guid="7b8107fd-3152-5d6e-b442-f47dc092b256",
    key="EX1",
    name="Rainbow Energy",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=95,
    set_code="EX1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    on_attach=rainbow_on_attach,
)
