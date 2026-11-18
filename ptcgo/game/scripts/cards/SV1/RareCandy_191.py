from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import rare_candy

card = ItemCardDef(
    guid="bb85c9d1-b889-5717-9de3-f09edb5f0678",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=191,
    set_code="SV1",
    rarity=Rarities.Common,
    effect=rare_candy()
)
