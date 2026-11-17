from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="3955c55d-0b1f-5717-94fe-9e9112440b57",
    key="COL1",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="COL1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False
)
