from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import escape_rope

card = ItemCardDef(
    guid="0f8cc060-a325-5258-96d4-c4e3baff5996",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EscapeRope.Name",
    display_name="Escape Rope",
    searchable_by=["Escape Rope", "Item"],
    subtypes=["Item"],
    collector_number=163,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    effect=escape_rope
)
