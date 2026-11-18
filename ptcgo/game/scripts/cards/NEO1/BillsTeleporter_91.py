from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n, if_heads

card = ItemCardDef(
    guid="47e96095-de5b-5f8d-8798-45ccfed56b02",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsTeleporter.Name",
    display_name="Bill's Teleporter",
    searchable_by=["Bill's Teleporter"],
    subtypes=[],
    collector_number=91,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    effect=if_heads(draw_n(4))
)
