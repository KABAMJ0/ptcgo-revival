from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import rare_candy

card = ItemCardDef(
    guid="7458a824-ff59-5099-a691-d079ae340c08",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="SV4PT5",
    rarity=Rarities.Common,
    effect=rare_candy()
)
