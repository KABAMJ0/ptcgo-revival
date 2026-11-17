from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_is_last, turn_damage_boost

card = SupporterCardDef(
    guid="b76f8111-e02b-5252-9132-5cd88b96e248",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GladionsFinalBattle.Name",
    display_name="Gladion's Final Battle",
    searchable_by=["Gladion's Final Battle", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    effect=turn_damage_boost(80, exclude_rule_box=True), condition=hand_is_last()
)
