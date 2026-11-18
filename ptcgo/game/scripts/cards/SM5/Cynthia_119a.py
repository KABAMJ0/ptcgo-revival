from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_draw

card = SupporterCardDef(
    guid="64b75b5f-83c1-573e-865f-8cf13b9f667e",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw(6)
)
