from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_until_tails_draw

card = ItemCardDef(
    guid="d55a84b8-e829-59e9-b5ad-4385c293296b",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name",
    display_name="Gym Badge",
    searchable_by=["Gym Badge", "Item"],
    subtypes=["Item"],
    collector_number=203,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    effect=flip_until_tails_draw(1)
)
