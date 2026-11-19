from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.card_effects.trainers import temp_attack_boost_for_named
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="ef622217-068c-5818-9591-e1f69689b011",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Misty.Name",
    display_name="Misty",
    searchable_by=["Misty"],
    subtypes=[],
    collector_number=18,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    play_cost=2,
    effect=temp_attack_boost_for_named("Misty", 20)
)
