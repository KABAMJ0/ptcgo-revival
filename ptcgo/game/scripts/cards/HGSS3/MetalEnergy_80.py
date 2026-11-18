from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f3008ce7-df97-543e-834c-3fd6d4df7bf2",
    key="HGSS3",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=80,
    set_code="HGSS3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
