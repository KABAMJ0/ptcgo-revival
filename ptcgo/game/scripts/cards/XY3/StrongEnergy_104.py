from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import pokemon_of_type
card = EnergyCardDef(
    guid="fc0679c9-79b4-5356-96e0-621c6296dabb",
    key="XY3",
    name="Strong Energy",
    display_name="Strong Energy",
    searchable_by=["Strong Energy", "Special"],
    subtypes=["Special"],
    collector_number=104,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=pokemon_of_type(PokemonTypes.FIGHTING),
)
