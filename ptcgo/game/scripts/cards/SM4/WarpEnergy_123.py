from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import warp_on_attach
card = EnergyCardDef(
    guid="a0cf3f3d-63c0-5396-bbaf-d1d4b1aa7ef6",
    key="SM4",
    name="Warp Energy",
    display_name="Warp Energy",
    searchable_by=["Warp Energy", "Special"],
    subtypes=["Special"],
    collector_number=123,
    set_code="SM4",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=warp_on_attach,
)
