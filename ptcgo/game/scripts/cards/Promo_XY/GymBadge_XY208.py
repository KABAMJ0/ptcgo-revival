from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_until_tails_draw

card = ItemCardDef(
    guid="0527456a-4dae-5504-be0a-fce98650295e",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name",
    display_name="Gym Badge",
    searchable_by=["Gym Badge", "Item"],
    subtypes=["Item"],
    collector_number=208,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    effect=flip_until_tails_draw(1)
)
