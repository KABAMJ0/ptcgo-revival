from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import heal_on_attach
card = EnergyCardDef(
    guid="972c2e95-aabc-569f-b109-2c1af9875f55",
    key="DP5",
    name="Health Energy",
    display_name="Health Energy",
    searchable_by=["Health Energy", "Special"],
    subtypes=["Special"],
    collector_number=94,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=heal_on_attach(1),
)
