from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_where

card = ItemCardDef(
    guid="af9cff4b-a4ad-533d-8618-170449b8f35e",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brock.Name",
    display_name="Brock",
    searchable_by=["Brock"],
    subtypes=[],
    collector_number=15,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    effect=heal_where(10, "each_own")
)
