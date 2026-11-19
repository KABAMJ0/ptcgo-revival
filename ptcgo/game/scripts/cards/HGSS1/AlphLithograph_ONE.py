from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_at_opponent_hand

card = ItemCardDef(
    guid="b37c6301-5c0e-50d6-a240-a9b3d0f94a34",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AlphLithograph.Name",
    display_name="Alph Lithograph",
    searchable_by=["Alph Lithograph", "Item"],
    subtypes=["Item"],
    collector_number=0,
    set_code="HGSS1",
    rarity=Rarities.RareSecret,
    effect=look_at_opponent_hand()
)
