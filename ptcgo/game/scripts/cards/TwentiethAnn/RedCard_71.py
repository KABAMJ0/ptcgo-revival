from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_shuffle_hand_draw

card = ItemCardDef(
    guid="e5e855ca-2af9-536e-a349-7dcf5d43bfc1",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedCard.Name",
    display_name="Red Card",
    searchable_by=["Red Card", "Item"],
    subtypes=["Item"],
    collector_number=71,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=opponent_shuffle_hand_draw(4)
)
