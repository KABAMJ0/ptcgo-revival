from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import DOUBLE_COLORLESS
card = EnergyCardDef(
    guid="762fc024-3a02-57de-ab81-0404aff13b81",
    key="BASE4",
    name="Double Colorless Energy",
    display_name="Double Colorless Energy",
    searchable_by=["Double Colorless Energy", "Special"],
    subtypes=["Special"],
    collector_number=124,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=DOUBLE_COLORLESS,
)
