from ptcgo.game.card_effects.trainers import sabrina_brycen
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="54a7c071-836c-55d3-840c-e06814f569c5",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinaBrycen.Name",
    display_name="Sabrina & Brycen",
    searchable_by=["Sabrina & Brycen", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=246,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    effect=sabrina_brycen()
)
