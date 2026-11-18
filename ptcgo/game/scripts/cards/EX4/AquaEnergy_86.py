from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities


from ptcgo.game.card_effects.energies import pokemon_named_like, pairs_of
card = EnergyCardDef(
    guid="09dd569f-37fa-567a-8b4e-662d8927d9e9",
    key="EX4",
    name="Aqua Energy",
    display_name="Aqua Energy",
    searchable_by=["Aqua Energy", "Special"],
    subtypes=["Special"],
    collector_number=86,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=pokemon_named_like("Team Aqua"),
    provides=pairs_of(PokemonTypes.WATER, PokemonTypes.DARKNESS),
)
