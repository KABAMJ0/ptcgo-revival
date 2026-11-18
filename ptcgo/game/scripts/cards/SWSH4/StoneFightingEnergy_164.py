from ptcgo.game.card_effects.energies import DamageReductionPassive
from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="547148db-8548-5873-a23b-fab024ff43d0",
    key="SWSH4",
    name="Stone Fighting Energy",
    display_name="Stone Fighting Energy",
    searchable_by=["Stone Fighting Energy", "Special"],
    subtypes=["Special"],
    collector_number=164,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.FIGHTING,
    is_special=True,
    passive=DamageReductionPassive(20, PokemonTypes.FIGHTING),
)
