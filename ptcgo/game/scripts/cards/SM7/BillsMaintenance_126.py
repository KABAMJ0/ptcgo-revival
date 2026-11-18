from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_one_hand_draw

card = SupporterCardDef(
    guid="e00628fa-11fb-58c3-9b08-38955c6747ab",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsMaintenance.Name",
    display_name="Bill's Maintenance",
    searchable_by=["Bill's Maintenance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=126,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=shuffle_one_hand_draw(3)
)
