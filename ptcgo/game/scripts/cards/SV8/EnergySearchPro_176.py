from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, search_distinct_types

card = ItemCardDef(
    guid="334ba6be-b93f-5519-8b7a-6c6fc1746d06",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearchPro.Name",
    display_name="Energy Search Pro",
    searchable_by=["Energy Search Pro", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=176,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=search_distinct_types(is_basic_energy_card, 9)
)
