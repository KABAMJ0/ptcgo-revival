from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_is_last, turn_damage_boost

card = SupporterCardDef(
    guid="7c486dff-3744-5b10-bbc1-1a8267ed1e29",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GladionsFinalBattle.Name",
    display_name="Gladion's Final Battle",
    searchable_by=["Gladion's Final Battle", "Supporter"],
    subtypes=["Supporter"],
    collector_number=118,
    set_code="ME5",
    rarity=Rarities.Rare,
    effect=turn_damage_boost(80, exclude_rule_box=True), condition=hand_is_last()
)
