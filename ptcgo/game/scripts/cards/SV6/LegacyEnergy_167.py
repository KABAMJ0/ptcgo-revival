from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="a7faf6d1-a217-596c-8ef1-551b8174fad3",
    key="SV6",
    name="Legacy Energy",
    display_name="Legacy Energy",
    searchable_by=["Legacy Energy", "Special", "ACE SPEC"],
    subtypes=["Special", "ACE SPEC"],
    collector_number=167,
    set_code="SV6",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
