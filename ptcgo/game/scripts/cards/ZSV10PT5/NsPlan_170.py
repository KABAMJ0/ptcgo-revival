from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_energy_to_active

card = SupporterCardDef(
    guid="177926f1-ac8f-5466-88ff-7be62b028964",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NsPlan.Name",
    display_name="N's Plan",
    searchable_by=["N's Plan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=170,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    effect=move_energy_to_active(2)
)
