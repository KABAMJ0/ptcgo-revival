from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import evolved_excluding_ex
card = EnergyCardDef(
    guid="0d62d22f-8e27-53d8-8db0-4af214e10eed",
    key="EX9",
    name="Double Rainbow Energy",
    display_name="Double Rainbow Energy",
    searchable_by=["Double Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=87,
    set_code="EX9",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=evolved_excluding_ex,
)
