from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_cards_draw

card = ItemCardDef(
    guid="66adede1-9e5d-5255-9003-2fd6298d0c60",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maintenance.Name",
    display_name="Maintenance",
    searchable_by=["Maintenance"],
    subtypes=[],
    collector_number=112,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_cards_draw(2, 1)
)
