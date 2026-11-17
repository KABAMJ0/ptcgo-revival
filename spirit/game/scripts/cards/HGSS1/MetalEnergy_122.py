from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c99c0fbc-4d36-5a02-9238-012dcc9f9a13",
    key="HGSS1",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="HGSS1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.METAL,
    is_special=False
)
