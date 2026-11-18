from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import DamageReductionPassive
card = EnergyCardDef(
    guid="d71cf934-bb13-5069-9f38-4c4079d6f42f",
    key="PL2",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=100,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=DamageReductionPassive(10, PokemonTypes.METAL),
)
