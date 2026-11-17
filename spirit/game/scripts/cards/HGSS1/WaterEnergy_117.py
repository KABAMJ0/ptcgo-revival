from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="883291ab-0eaa-59b2-859c-e472233579ea",
    key="HGSS1",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="HGSS1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.WATER,
    is_special=False
)
