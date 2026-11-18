from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import MetalEnergyLegacyPassive
card = EnergyCardDef(
    guid="eecf2044-33f1-592a-bae9-9ebe70d45c5a",
    key="ECARD1",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=159,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=MetalEnergyLegacyPassive(),
)
