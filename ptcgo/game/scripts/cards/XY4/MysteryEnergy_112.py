from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="e85fead9-af5a-5f80-a84b-dede2d56e2d3",
    key="XY4",
    name="Mystery Energy",
    display_name="Mystery Energy",
    searchable_by=["Mystery Energy", "Special"],
    subtypes=["Special"],
    collector_number=112,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
