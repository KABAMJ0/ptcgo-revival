from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.card_effects.trainers import is_energy_card, named_one_of

card = SupporterCardDef(
    guid="c9f5e4ac-36a4-5da9-acf1-d84198fbd72e",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksTraining.Name",
    display_name="Brock's Training",
    searchable_by=["Brock's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=55,
    set_code="HF",
    rarity=Rarities.RareHolo,
    effect=attach_from_hand(is_energy_card, count=1, target="choice", target_pred=named_one_of("Geodude", "Graveler", "Golem", "Onix-GX", "Cubone", "Rhyhorn", "Rhydon", "Sudowoodo"))
)
