from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_hand_to_bottom_draw_same

card = ItemCardDef(
    guid="a6084b29-e8d0-5287-93c4-1d2c316dfec4",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PeekingRedCard.Name",
    display_name="Peeking Red Card",
    searchable_by=["Peeking Red Card", "Item"],
    subtypes=["Item"],
    collector_number=169,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    effect=opponent_hand_to_bottom_draw_same(optional=True)
)
