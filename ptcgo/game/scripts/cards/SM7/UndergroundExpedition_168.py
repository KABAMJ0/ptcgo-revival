from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_bottom_to_hand

card = SupporterCardDef(
    guid="50cfd7d5-0839-5841-b2aa-3702bb9caac1",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UndergroundExpedition.Name",
    display_name="Underground Expedition",
    searchable_by=["Underground Expedition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=168,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=look_bottom_to_hand(4, 2, None)
)
