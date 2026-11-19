from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.card_effects.trainers import temp_attack_boost_for_named
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="0494fa5d-d688-54ea-832d-ab1dcf236f05",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Misty.Name",
    display_name="Misty",
    searchable_by=["Misty"],
    subtypes=[],
    collector_number=18,
    set_code="ME55C",
    rarity=Rarities.RareHolo,
    play_cost=2,
    effect=temp_attack_boost_for_named("Misty", 20)
)
