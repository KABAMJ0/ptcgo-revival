from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_opponent_hand_to

card = SupporterCardDef(
    guid="adecffaa-a40b-5190-aa8d-0aca5542ddaf",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.XerosicsMachinations.Name",
    display_name="Xerosic's Machinations",
    searchable_by=["Xerosic's Machinations", "Supporter"],
    subtypes=["Supporter"],
    collector_number=64,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    effect=discard_opponent_hand_to(3)
)
