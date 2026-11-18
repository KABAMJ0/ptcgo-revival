from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import cyclone_on_attach
card = EnergyCardDef(
    guid="243cf2a0-6b66-5548-b9d3-65ae824a1452",
    key="EX16",
    name="Cyclone Energy",
    display_name="Cyclone Energy",
    searchable_by=["Cyclone Energy", "Special"],
    subtypes=["Special"],
    collector_number=90,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=cyclone_on_attach,
)
