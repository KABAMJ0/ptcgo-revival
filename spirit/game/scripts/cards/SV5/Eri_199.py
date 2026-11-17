from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_from_opponent_hand, is_item_card

card = SupporterCardDef(
    guid="2bf599ea-1346-509e-9777-4c927c2e7fca",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eri.Name",
    display_name="Eri",
    searchable_by=["Eri", "Supporter"],
    subtypes=["Supporter"],
    collector_number=199,
    set_code="SV5",
    rarity=Rarities.Rare,
    effect=discard_from_opponent_hand(predicate=is_item_card, count=2)
)
