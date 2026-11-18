from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import one_at_a_time
card = EnergyCardDef(
    guid="3c3d32a5-7dea-5595-b386-57d020e8aa14",
    key="BW6",
    name="Blend Energy WaterLightningFightingMetal",
    display_name="Blend Energy WaterLightningFightingMetal",
    searchable_by=["Blend Energy WaterLightningFightingMetal", "Special"],
    subtypes=["Special"],
    collector_number=118,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=one_at_a_time(PokemonTypes.WATER, PokemonTypes.LIGHTNING, PokemonTypes.FIGHTING, PokemonTypes.METAL),
)
