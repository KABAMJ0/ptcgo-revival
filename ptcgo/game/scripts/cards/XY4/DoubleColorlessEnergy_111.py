from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import DOUBLE_COLORLESS
card = EnergyCardDef(
    guid="30bf569c-5189-52c4-8a9f-bd63977f9634",
    key="XY4",
    name="Double Colorless Energy",
    display_name="Double Colorless Energy",
    searchable_by=["Double Colorless Energy", "Special"],
    subtypes=["Special"],
    collector_number=111,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=DOUBLE_COLORLESS,
)
