from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_to_bottom_draw_until

card = SupporterCardDef(
    guid="089f8d41-b5de-55f7-a75a-4d72775738be",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dendra.Name",
    display_name="Dendra",
    searchable_by=["Dendra", "Supporter"],
    subtypes=["Supporter"],
    collector_number=179,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    effect=hand_to_bottom_draw_until(5)
)
