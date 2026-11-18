from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import one_at_a_time
card = EnergyCardDef(
    guid="f2afe5b0-5b2c-5c33-9e77-101b595436ad",
    key="SM6",
    name="Unit Energy FightingDarknessFairy",
    display_name="Unit Energy FightingDarknessFairy",
    searchable_by=["Unit Energy FightingDarknessFairy", "Special"],
    subtypes=["Special"],
    collector_number=146,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=one_at_a_time(PokemonTypes.FIGHTING, PokemonTypes.DARKNESS, PokemonTypes.FAIRY),
)
