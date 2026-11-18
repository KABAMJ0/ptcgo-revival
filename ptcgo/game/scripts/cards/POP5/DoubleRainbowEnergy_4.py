from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import evolved_excluding_ex
card = EnergyCardDef(
    guid="d2a27312-d2db-5b96-8be2-e2dd9a2f4674",
    key="POP5",
    name="Double Rainbow Energy",
    display_name="Double Rainbow Energy",
    searchable_by=["Double Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=4,
    set_code="POP5",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=evolved_excluding_ex,
)
