from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_in_play, is_stadium_card, is_tool_card

card = ItemCardDef(
    guid="bfaa43c6-8b9a-5b7d-bc98-34bfb2adf7f7",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieldBlower.Name",
    display_name="Field Blower",
    searchable_by=["Field Blower", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=discard_in_play([is_tool_card, is_stadium_card], count=2)
)
