from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_switch_then_self_switch

card = SupporterCardDef(
    guid="7e572dfe-c58b-53b0-86bb-85b34e9b275b",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Guzma.Name",
    display_name="Guzma",
    searchable_by=["Guzma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=115,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=opponent_switch_then_self_switch()
)
