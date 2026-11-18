from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import DamageReductionPassive
card = EnergyCardDef(
    guid="48984c1f-2f3c-5a05-b83f-72bc60d99726",
    key="EX13",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=95,
    set_code="EX13",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=DamageReductionPassive(10, PokemonTypes.METAL),
)
