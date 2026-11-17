from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="494beb4a-ca18-526e-ba1f-93e0f60135e0",
    key="G1",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="G1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.GRASS,
    is_special=False
)
