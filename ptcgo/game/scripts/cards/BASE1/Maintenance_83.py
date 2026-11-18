from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_cards_draw

card = ItemCardDef(
    guid="637b0637-f28f-5e86-879f-a65742999194",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maintenance.Name",
    display_name="Maintenance",
    searchable_by=["Maintenance"],
    subtypes=[],
    collector_number=83,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_cards_draw(2, 1)
)
