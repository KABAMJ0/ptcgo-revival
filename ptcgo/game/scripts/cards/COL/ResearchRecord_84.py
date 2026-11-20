from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import research_record

card = ItemCardDef(
    guid="d31b1943-452c-54a0-b602-16d652bf348f",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ResearchRecord.Name",
    display_name="Research Record",
    searchable_by=["Research Record", "Item"],
    subtypes=["Item"],
    collector_number=84,
    set_code="COL",
    rarity=Rarities.Uncommon,
    effect=research_record
)
