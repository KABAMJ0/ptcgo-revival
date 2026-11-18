from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import one_at_a_time
card = EnergyCardDef(
    guid="9f76473e-f1f3-5716-a5cb-2585356db109",
    key="BW6",
    name="Blend Energy GrassFirePsychicDarkness",
    display_name="Blend Energy GrassFirePsychicDarkness",
    searchable_by=["Blend Energy GrassFirePsychicDarkness", "Special"],
    subtypes=["Special"],
    collector_number=117,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=one_at_a_time(PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.PSYCHIC, PokemonTypes.DARKNESS),
)
