from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import SuperBoostEnergyPassive
card = EnergyCardDef(
    guid="2a37d903-7ba4-5b1b-a10c-41793795b9a4",
    key="SM5",
    name="Super Boost Energy ◇",
    display_name="Super Boost Energy ◇",
    searchable_by=["Super Boost Energy \u25c7", "Special", "Prism Star"],
    subtypes=["Special", "Prism Star"],
    collector_number=136,
    set_code="SM5",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=SuperBoostEnergyPassive(),
)
