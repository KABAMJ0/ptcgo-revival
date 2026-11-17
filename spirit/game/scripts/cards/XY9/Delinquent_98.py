from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_stadium_then_opponent_discards

card = SupporterCardDef(
    guid="69bcc164-329e-5742-b18a-d8992a01cef1",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Delinquent.Name",
    display_name="Delinquent",
    searchable_by=["Delinquent", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=discard_stadium_then_opponent_discards(3)
)
