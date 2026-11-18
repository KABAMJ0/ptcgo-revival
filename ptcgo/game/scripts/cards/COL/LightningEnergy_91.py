from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="a7fcb8fd-ff24-56c3-8c43-9c7b393b15a4",
    key="COL",
    name="Lightning Energy",
    display_name="Lightning Energy",
    searchable_by=["Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="COL",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False
)
