from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import revive_with_damage

card = ItemCardDef(
    guid="b45cab76-43ab-53db-87d5-790f3ac63c9a",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revive.Name",
    display_name="Revive",
    searchable_by=["Revive"],
    subtypes=[],
    collector_number=89,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    effect=revive_with_damage(1)
)
