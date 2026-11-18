from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import recycle_from_discard

card = ItemCardDef(
    guid="dc249005-d213-5514-864f-90704c0ca770",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Recycle.Name",
    display_name="Recycle",
    searchable_by=["Recycle"],
    subtypes=[],
    collector_number=61,
    set_code="BASE3",
    rarity=Rarities.Common,
    effect=recycle_from_discard(1)
)
