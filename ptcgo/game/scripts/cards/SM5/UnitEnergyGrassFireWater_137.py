from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="78ef6670-b1f2-537d-9da9-f631e193cb2f",
    key="SM5",
    name="Unit Energy GrassFireWater",
    display_name="Unit Energy GrassFireWater",
    searchable_by=["Unit Energy GrassFireWater", "Special"],
    subtypes=["Special"],
    collector_number=137,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
