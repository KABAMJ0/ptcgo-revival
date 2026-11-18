from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_shuffle_draw_per_prize

card = ItemCardDef(
    guid="e3994ea5-b641-5ba5-b27e-d0f035ad508e",
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
