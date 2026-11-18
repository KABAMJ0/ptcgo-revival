from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import rare_candy

card = ItemCardDef(
    guid="5bb13402-bfe3-5b9d-8e6a-85d972eee473",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=256,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=rare_candy()
)
