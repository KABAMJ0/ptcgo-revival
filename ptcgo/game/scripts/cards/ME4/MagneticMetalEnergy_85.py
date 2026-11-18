from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="ee6accee-0629-5f76-8b93-66c6fc9b2e74",
    key="ME4",
    name="Magnetic Metal Energy",
    display_name="Magnetic Metal Energy",
    searchable_by=["Magnetic Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=85,
    set_code="ME4",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
