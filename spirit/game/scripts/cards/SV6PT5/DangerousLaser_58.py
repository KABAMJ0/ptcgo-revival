from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import SpecialConditions, condition_opponent_active

card = ItemCardDef(
    guid="2378f35e-224b-53df-957c-37e5c81a81c0",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DangerousLaser.Name",
    display_name="Dangerous Laser",
    searchable_by=["Dangerous Laser", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=58,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    effect=condition_opponent_active(SpecialConditions.BURNED, SpecialConditions.CONFUSED)
)
