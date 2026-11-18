from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_one_hand_draw

card = SupporterCardDef(
    guid="f93312cf-60e9-5de6-8804-e9b62e2403bf",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsMaintenance.Name",
    display_name="Bill's Maintenance",
    searchable_by=["Bill's Maintenance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=shuffle_one_hand_draw(3)
)
