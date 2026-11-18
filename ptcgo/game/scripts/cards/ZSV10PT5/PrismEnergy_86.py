from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import PrismEnergyPassive
card = EnergyCardDef(
    guid="f7570c28-92a7-5fe1-9fdb-901004795357",
    key="ZSV10PT5",
    name="Prism Energy",
    display_name="Prism Energy",
    searchable_by=["Prism Energy", "Special"],
    subtypes=["Special"],
    collector_number=86,
    set_code="ZSV10PT5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=PrismEnergyPassive(),
)
