from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_opponent_hand_to

card = SupporterCardDef(
    guid="0a20d0ea-1501-5e9b-a738-100247a8bd62",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.XerosicsMachinations.Name",
    display_name="Xerosic's Machinations",
    searchable_by=["Xerosic's Machinations", "Supporter"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    effect=discard_opponent_hand_to(3)
)
