from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="61b7bdfa-01c8-5ee4-9b0c-eb8a7032dccf",
    key="SV2",
    name="Reversal Energy",
    display_name="Reversal Energy",
    searchable_by=["Reversal Energy", "Special"],
    subtypes=["Special"],
    collector_number=192,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
