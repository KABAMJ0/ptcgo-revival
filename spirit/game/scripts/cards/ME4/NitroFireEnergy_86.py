from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f37baa9f-6e68-5ced-b448-25a5c47d7844",
    key="ME4",
    name="Nitro Fire Energy",
    display_name="Nitro Fire Energy",
    searchable_by=["Nitro Fire Energy", "Special"],
    subtypes=["Special"],
    collector_number=86,
    set_code="ME4",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
