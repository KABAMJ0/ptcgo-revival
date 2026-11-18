from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import heal_on_attach
card = EnergyCardDef(
    guid="d21cdcec-701a-5e06-b618-9e274b71ad4d",
    key="BASE6",
    name="Potion Energy",
    display_name="Potion Energy",
    searchable_by=["Potion Energy", "Special"],
    subtypes=["Special"],
    collector_number=101,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=heal_on_attach(1),
)
