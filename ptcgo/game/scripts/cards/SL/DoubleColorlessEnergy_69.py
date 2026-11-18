from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import DOUBLE_COLORLESS
card = EnergyCardDef(
    guid="18304303-0e90-5375-a433-903b530e7ac8",
    key="SL",
    name="Double Colorless Energy",
    display_name="Double Colorless Energy",
    searchable_by=["Double Colorless Energy", "Special"],
    subtypes=["Special"],
    collector_number=69,
    set_code="SL",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=DOUBLE_COLORLESS,
)
