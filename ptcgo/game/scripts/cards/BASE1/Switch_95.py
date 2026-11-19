from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import switch

card = ItemCardDef(
    guid="bc14dcbb-a491-5309-8c29-31cddb6a371b",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch"],
    subtypes=[],
    collector_number=95,
    set_code="BASE1",
    rarity=Rarities.Common,
    effect=switch
)
