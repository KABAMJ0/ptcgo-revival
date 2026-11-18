from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_where

card = ItemCardDef(
    guid="08202675-968e-51ca-a73b-ed173c4f300d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brock.Name",
    display_name="Brock",
    searchable_by=["Brock"],
    subtypes=[],
    collector_number=98,
    set_code="GYM1",
    rarity=Rarities.Rare,
    effect=heal_where(10, "each_own")
)
