from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="24a74c0e-4d7d-5bd4-8f8d-e71304f32c1c",
    key="HGSS1",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="HGSS1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False
)
