from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import cure_on_attach
card = EnergyCardDef(
    guid="36fcba75-b803-5ffb-8ae5-e62c34df7ec0",
    key="DP5",
    name="Recover Energy",
    display_name="Recover Energy",
    searchable_by=["Recover Energy", "Special"],
    subtypes=["Special"],
    collector_number=96,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=cure_on_attach,
)
