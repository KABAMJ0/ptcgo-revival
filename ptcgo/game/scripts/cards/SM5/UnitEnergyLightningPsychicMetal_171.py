from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import one_at_a_time
card = EnergyCardDef(
    guid="a442d5d3-b4ab-5ae9-a6de-246c31e31503",
    key="SM5",
    name="Unit Energy LightningPsychicMetal",
    display_name="Unit Energy LightningPsychicMetal",
    searchable_by=["Unit Energy LightningPsychicMetal", "Special"],
    subtypes=["Special"],
    collector_number=171,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=one_at_a_time(PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.METAL),
)
