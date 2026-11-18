from ptcgo.game.card_effects.energies import heal_on_attach
from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="e019489d-abe6-5bed-aef5-91b1219a4a1d",
    key="SV4",
    name="Medical Energy",
    display_name="Medical Energy",
    searchable_by=["Medical Energy", "Special"],
    subtypes=["Special"],
    collector_number=182,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=heal_on_attach(3),
)
