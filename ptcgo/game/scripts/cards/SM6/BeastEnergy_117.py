from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import SubtypeProvisionPassive
card = EnergyCardDef(
    guid="615041ff-89b0-5924-830e-a810d82285ad",
    key="SM6",
    name="Beast Energy ◇",
    display_name="Beast Energy ◇",
    searchable_by=["Beast Energy \u25c7", "Special", "Prism Star"],
    subtypes=["Special", "Prism Star"],
    collector_number=117,
    set_code="SM6",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=SubtypeProvisionPassive("Ultra Beast"),
)
