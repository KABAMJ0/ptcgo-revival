from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attach_darkness_to_each_poison

card = SupporterCardDef(
    guid="b0de01c2-33d8-5916-b6c3-8051490abd27",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JaninesSecretArt.Name",
    display_name="Janine's Secret Art",
    searchable_by=["Janine's Secret Art", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    effect=attach_darkness_to_each_poison()
)
