from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="aaad2f1e-24f3-55b7-90fe-81c874a15a77",
    key="HGSS3",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=79,
    set_code="HGSS3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
