from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_where

card = ItemCardDef(
    guid="9bec5e9a-9517-5731-9913-908829d4d8b3",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PicnicBasket.Name",
    display_name="Picnic Basket",
    searchable_by=["Picnic Basket", "Item"],
    subtypes=["Item"],
    collector_number=184,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=heal_where(30, "each_both")
)
