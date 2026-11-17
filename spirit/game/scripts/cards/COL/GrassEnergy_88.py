from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="29c5b746-0f71-536c-89d1-76a7541b293f",
    key="COL",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="COL",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.GRASS,
    is_special=False
)
