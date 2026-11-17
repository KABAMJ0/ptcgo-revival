from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_switch_then_self_switch

card = SupporterCardDef(
    guid="329d52ad-13e4-5415-8188-eedf45478eca",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Guzma.Name",
    display_name="Guzma",
    searchable_by=["Guzma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=143,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    effect=opponent_switch_then_self_switch()
)
