from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import MetalEnergyLegacyPassive
card = EnergyCardDef(
    guid="9f9d6315-9756-59b0-a68b-28795c93ef45",
    key="NEO1",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=19,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=MetalEnergyLegacyPassive(),
)
