from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="17c48446-a285-5025-b169-6bff4c0db60e",
    key="SV1",
    name="Basic Lightning Energy",
    display_name="Basic Lightning Energy",
    searchable_by=["Basic Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=257,
    set_code="SV1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False
)
