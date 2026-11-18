from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import buddy_buddy_rescue

card = ItemCardDef(
    guid="621b05a3-ec94-5aaf-ba07-099dfe7b2b54",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BuddyBuddyRescue.Name",
    display_name="Buddy-Buddy Rescue",
    searchable_by=["Buddy-Buddy Rescue", "Item"],
    subtypes=["Item"],
    collector_number=135,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=buddy_buddy_rescue(1)
)
