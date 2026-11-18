from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5389cfad-55a2-5bce-813e-25debf5dd28a",
    key="BASE6",
    name="Full Heal Energy",
    display_name="Full Heal Energy",
    searchable_by=["Full Heal Energy", "Special"],
    subtypes=["Special"],
    collector_number=100,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
