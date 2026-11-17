from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_stadium_then_opponent_discards

card = SupporterCardDef(
    guid="5555d1d1-0a03-5414-9173-a4cd85caf68d",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Delinquent.Name",
    display_name="Delinquent",
    searchable_by=["Delinquent", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    effect=discard_stadium_then_opponent_discards(3)
)
