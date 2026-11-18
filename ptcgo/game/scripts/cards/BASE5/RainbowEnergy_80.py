from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="3bdd8e5f-c47b-5981-a1c4-41b0a36a7e74",
    key="BASE5",
    name="Rainbow Energy",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=80,
    set_code="BASE5",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
