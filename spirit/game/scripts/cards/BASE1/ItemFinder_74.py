from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_trainer_card, with_discard_cost

card = ItemCardDef(
    guid="614c8467-8be1-5f23-bb8b-989ddf3bf261",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ItemFinder.Name",
    display_name="Item Finder",
    searchable_by=["Item Finder"],
    subtypes=[],
    collector_number=74,
    set_code="BASE1",
    rarity=Rarities.Rare,
    effect=with_discard_cost(2, recover_from_discard(is_trainer_card, count=1, to="hand"))
)
