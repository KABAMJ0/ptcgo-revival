from ptcgo.game.card_effects.energies import pairs_of, pokemon_named_like
from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="94bd80de-a4be-5a50-8ecf-0787d5c67b3c",
    key="SV10",
    name="Team Rocket's Energy",
    display_name="Team Rocket's Energy",
    searchable_by=["Team Rocket's Energy", "Special"],
    subtypes=["Special"],
    collector_number=182,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=pokemon_named_like("Team Rocket"),
    provides=pairs_of(PokemonTypes.PSYCHIC, PokemonTypes.DARKNESS),
)
