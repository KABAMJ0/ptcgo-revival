from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import evolved_excluding_ex
card = EnergyCardDef(
    guid="1bbb4313-687a-584d-8da4-785ff1818e26",
    key="EX14",
    name="Double Rainbow Energy",
    display_name="Double Rainbow Energy",
    searchable_by=["Double Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=88,
    set_code="EX14",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=evolved_excluding_ex,
)
