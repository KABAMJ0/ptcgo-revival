from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="eddd0f03-fb27-5e55-8fea-001ba1444690",
    key="ME2PT5",
    name="Prism Energy",
    display_name="Prism Energy",
    searchable_by=["Prism Energy", "Special"],
    subtypes=["Special"],
    collector_number=216,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
