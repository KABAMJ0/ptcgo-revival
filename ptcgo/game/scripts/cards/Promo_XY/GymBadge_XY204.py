from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_until_tails_draw

card = ItemCardDef(
    guid="2cf8c910-9134-5a0b-a0ec-21c70c140bf6",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name",
    display_name="Gym Badge",
    searchable_by=["Gym Badge", "Item"],
    subtypes=["Item"],
    collector_number=204,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    effect=flip_until_tails_draw(1)
)
