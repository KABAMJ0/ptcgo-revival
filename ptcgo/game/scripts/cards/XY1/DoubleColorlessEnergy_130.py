from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import DOUBLE_COLORLESS
card = EnergyCardDef(
    guid="5c47616e-2e51-5bc9-90ab-7d41fe54b681",
    key="XY1",
    name="Double Colorless Energy",
    display_name="Double Colorless Energy",
    searchable_by=["Double Colorless Energy", "Special"],
    subtypes=["Special"],
    collector_number=130,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=DOUBLE_COLORLESS,
)
