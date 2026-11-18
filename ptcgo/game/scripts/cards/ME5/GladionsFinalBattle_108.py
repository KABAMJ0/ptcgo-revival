from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_is_last, turn_damage_boost

card = SupporterCardDef(
    guid="a994f8a1-c3f8-5ab7-987d-f4e972ac9a11",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GladionsFinalBattle.Name",
    display_name="Gladion's Final Battle",
    searchable_by=["Gladion's Final Battle", "Supporter"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="ME5",
    rarity=Rarities.Rare,
    effect=turn_damage_boost(80, exclude_rule_box=True), condition=hand_is_last()
)
