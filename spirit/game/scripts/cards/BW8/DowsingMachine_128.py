from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_trainer_card, with_discard_cost

card = ItemCardDef(
    guid="b5f85814-dbe1-5495-bcda-cdee9d7f4442",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DowsingMachine.Name",
    display_name="Dowsing Machine",
    searchable_by=["Dowsing Machine", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=128,
    set_code="BW8",
    rarity=Rarities.Rare,
    effect=with_discard_cost(2, recover_from_discard(is_trainer_card, count=1, to="hand"))
)
