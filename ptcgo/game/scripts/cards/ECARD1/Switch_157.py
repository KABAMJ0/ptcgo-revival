from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import switch

card = ItemCardDef(
    guid="fff7fde6-46d5-5b23-b648-2904abcdc49d",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch"],
    subtypes=[],
    collector_number=157,
    set_code="ECARD1",
    rarity=Rarities.Common,
    effect=switch
)
