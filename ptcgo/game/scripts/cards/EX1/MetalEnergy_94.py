from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import DamageReductionPassive
card = EnergyCardDef(
    guid="fa12931b-5b2b-5a1e-9646-db2d695a4222",
    key="EX1",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=94,
    set_code="EX1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=DamageReductionPassive(10, PokemonTypes.METAL),
)
