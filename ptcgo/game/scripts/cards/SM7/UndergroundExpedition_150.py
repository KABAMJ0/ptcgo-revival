from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_bottom_to_hand

card = SupporterCardDef(
    guid="8e14809a-ab53-554a-8897-7c48c6b2b730",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UndergroundExpedition.Name",
    display_name="Underground Expedition",
    searchable_by=["Underground Expedition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_hand(4, 2, None)
)
