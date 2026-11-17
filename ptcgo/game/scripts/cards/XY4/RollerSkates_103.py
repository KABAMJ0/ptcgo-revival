from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n, if_heads

card = ItemCardDef(
    guid="f8f1569d-092a-56a8-8bdc-83f0902acc95",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RollerSkates.Name",
    display_name="Roller Skates",
    searchable_by=["Roller Skates", "Item"],
    subtypes=["Item"],
    collector_number=103,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=if_heads(draw_n(3))
)
