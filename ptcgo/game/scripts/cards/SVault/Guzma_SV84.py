from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_switch_then_self_switch

card = SupporterCardDef(
    guid="a285a3ee-6fc7-530e-a604-4615e2129712",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Guzma.Name",
    display_name="Guzma",
    searchable_by=["Guzma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=84,
    set_code="SVault",
    rarity=Rarities.RareUltra,
    effect=opponent_switch_then_self_switch()
)
