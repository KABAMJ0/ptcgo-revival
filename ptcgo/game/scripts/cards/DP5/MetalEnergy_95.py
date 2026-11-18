from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import DamageReductionPassive
card = EnergyCardDef(
    guid="abf26949-3d57-5aba-8faa-0c57be0cdb9f",
    key="DP5",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=95,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=DamageReductionPassive(10, PokemonTypes.METAL),
)
