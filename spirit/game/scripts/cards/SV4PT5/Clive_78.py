from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_per_opponent_hand_card, is_supporter_card

card = SupporterCardDef(
    guid="947eb103-dcce-563c-ba56-b9ea4e067858",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Clive.Name",
    display_name="Clive",
    searchable_by=["Clive", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    effect=draw_per_opponent_hand_card(predicate=is_supporter_card, per=2)
)
