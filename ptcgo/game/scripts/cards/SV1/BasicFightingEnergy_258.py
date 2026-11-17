from ptcgo.game.data_utils import EnergyCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="2376b90d-ccdb-5d30-b482-757a76c56aa0",
    key="SV1",
    name="Basic Fighting Energy",
    display_name="Basic Fighting Energy",
    searchable_by=["Basic Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=258,
    set_code="SV1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False
)
