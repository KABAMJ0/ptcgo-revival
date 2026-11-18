from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="1bd1bf3f-c2e1-5b3c-abc7-077d2721bb70",
    key="ECARD3",
    name="Retro Energy",
    display_name="Retro Energy",
    searchable_by=["Retro Energy", "Special"],
    subtypes=["Special"],
    collector_number=144,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
