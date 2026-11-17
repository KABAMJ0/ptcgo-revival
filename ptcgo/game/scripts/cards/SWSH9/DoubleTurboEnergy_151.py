from ptcgo.game.card_effects.energies import DoubleTurboPassive
from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f2c20770-b08b-5f5b-bb9a-7ec86ad399a6",
    key="SWSH9",
    name="Double Turbo Energy",
    display_name="Double Turbo Energy",
    searchable_by=["Double Turbo Energy", "Special"],
    subtypes=["Special"],
    collector_number=151,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
    passive=DoubleTurboPassive()
)
