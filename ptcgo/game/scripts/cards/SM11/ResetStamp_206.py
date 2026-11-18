from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_shuffle_draw_per_prize

card = ItemCardDef(
    guid="3e8493ff-cb8a-56ea-9246-910bd2e970ad",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ResetStamp.Name",
    display_name="Reset Stamp",
    searchable_by=["Reset Stamp", "Item"],
    subtypes=["Item"],
    collector_number=206,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=opponent_shuffle_draw_per_prize()
)
