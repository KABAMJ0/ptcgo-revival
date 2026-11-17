from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_in_play, is_stadium_card, is_tool_card

card = ItemCardDef(
    guid="872fae20-13e1-5379-a9e1-e929439f68e4",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieldBlower.Name",
    display_name="Field Blower",
    searchable_by=["Field Blower", "Item"],
    subtypes=["Item"],
    collector_number=163,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    effect=discard_in_play([is_tool_card, is_stadium_card], count=2)
)
