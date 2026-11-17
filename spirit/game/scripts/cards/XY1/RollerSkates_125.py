from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_n, if_heads

card = ItemCardDef(
    guid="762c8466-bfbb-5e0b-ab40-00861f03ed81",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RollerSkates.Name",
    display_name="Roller Skates",
    searchable_by=["Roller Skates", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=if_heads(draw_n(3))
)
