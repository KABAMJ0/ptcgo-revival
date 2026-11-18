from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import pokemon_of_type
card = EnergyCardDef(
    guid="8c8945f3-43a7-560c-9c0a-80cabe04ad53",
    key="XY5",
    name="Wonder Energy",
    display_name="Wonder Energy",
    searchable_by=["Wonder Energy", "Special"],
    subtypes=["Special"],
    collector_number=144,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=pokemon_of_type(PokemonTypes.FAIRY),
)
