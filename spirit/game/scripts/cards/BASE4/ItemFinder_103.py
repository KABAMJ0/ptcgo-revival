from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_trainer_card, with_discard_cost

card = ItemCardDef(
    guid="cdb60c14-3d35-5e77-b80e-0a88e9703f14",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ItemFinder.Name",
    display_name="Item Finder",
    searchable_by=["Item Finder"],
    subtypes=[],
    collector_number=103,
    set_code="BASE4",
    rarity=Rarities.Rare,
    effect=with_discard_cost(2, recover_from_discard(is_trainer_card, count=1, to="hand"))
)
