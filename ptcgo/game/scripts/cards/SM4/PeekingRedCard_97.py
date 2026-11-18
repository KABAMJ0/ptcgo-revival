from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_hand_to_bottom_draw_same

card = ItemCardDef(
    guid="b818ec09-ef33-5424-bd54-16aa869707a6",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PeekingRedCard.Name",
    display_name="Peeking Red Card",
    searchable_by=["Peeking Red Card", "Item"],
    subtypes=["Item"],
    collector_number=97,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    effect=opponent_hand_to_bottom_draw_same(optional=True)
)
