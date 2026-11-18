from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_bottom_to_hand

card = SupporterCardDef(
    guid="c94fa786-377c-52b3-82e6-41eeed9d1b6c",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UndergroundExpedition.Name",
    display_name="Underground Expedition",
    searchable_by=["Underground Expedition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=97,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_hand(4, 2, None)
)
