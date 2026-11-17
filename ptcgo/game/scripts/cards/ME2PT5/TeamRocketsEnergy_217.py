from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="757c69cc-f801-5531-a0a6-78c73733405c",
    key="ME2PT5",
    name="Team Rocket's Energy",
    display_name="Team Rocket's Energy",
    searchable_by=["Team Rocket's Energy", "Special"],
    subtypes=["Special"],
    collector_number=217,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
