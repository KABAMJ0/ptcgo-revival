from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_one_hand_draw

card = SupporterCardDef(
    guid="68a66fad-1440-5aec-aba0-6856f397b463",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsMaintenance.Name",
    display_name="Bill's Maintenance",
    searchable_by=["Bill's Maintenance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=71,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=shuffle_one_hand_draw(3)
)
