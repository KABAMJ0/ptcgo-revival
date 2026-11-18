from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import DOUBLE_COLORLESS
card = EnergyCardDef(
    guid="b03bd78a-5f96-53e5-82b5-717afbf9e2bf",
    key="XY10",
    name="Double Colorless Energy",
    display_name="Double Colorless Energy",
    searchable_by=["Double Colorless Energy", "Special"],
    subtypes=["Special"],
    collector_number=114,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=DOUBLE_COLORLESS,
)
