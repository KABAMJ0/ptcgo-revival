from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_hand_bottom_then_draw, opponent_prizes_at_most

card = ItemCardDef(
    guid="4e8d59dd-a91a-5f93-8a84-542bdc58d6a7",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpecialRedCard.Name",
    display_name="Special Red Card",
    searchable_by=["Special Red Card", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    effect=opponent_hand_bottom_then_draw(3), condition=opponent_prizes_at_most(3)
)
