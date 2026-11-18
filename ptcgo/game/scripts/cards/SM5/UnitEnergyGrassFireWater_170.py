from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import one_at_a_time
card = EnergyCardDef(
    guid="6045f77f-d7da-5ed4-864b-faea6c7c0f0b",
    key="SM5",
    name="Unit Energy GrassFireWater",
    display_name="Unit Energy GrassFireWater",
    searchable_by=["Unit Energy GrassFireWater", "Special"],
    subtypes=["Special"],
    collector_number=170,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=one_at_a_time(PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER),
)
