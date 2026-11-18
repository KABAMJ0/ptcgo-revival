from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import SubtypeProvisionPassive, SubtypeProvisionPassive
card = EnergyCardDef(
    guid="26e993bc-e807-54c4-a5c2-a548a3d1d081",
    key="PL2",
    name="SP Energy",
    display_name="SP Energy",
    searchable_by=["SP Energy", "Special"],
    subtypes=["Special"],
    collector_number=101,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=SubtypeProvisionPassive("SP"),
)
