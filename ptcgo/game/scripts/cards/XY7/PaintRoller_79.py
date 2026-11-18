from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_stadium_card, draw_after

card = ItemCardDef(
    guid="b15e2067-8360-58c1-b37c-ffea09f3bcd5",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PaintRoller.Name",
    display_name="Paint Roller",
    searchable_by=["Paint Roller", "Item"],
    subtypes=["Item"],
    collector_number=79,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    effect=draw_after(1, discard_stadium_card())
)
