from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import pokemon_of_type
card = EnergyCardDef(
    guid="2f0c1f4b-b09c-5cb4-9a43-a19803ede03e",
    key="XY6",
    name="Double Dragon Energy",
    display_name="Double Dragon Energy",
    searchable_by=["Double Dragon Energy", "Special"],
    subtypes=["Special"],
    collector_number=97,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=pokemon_of_type(PokemonTypes.DRAGON),
)
