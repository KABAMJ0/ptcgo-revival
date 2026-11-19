from ptcgo.game.card_effects.trainers import team_types_take_less_next_turn
from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="65756ebb-c3c2-531b-a5a8-26ced2fc6d10",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IronDefender.Name",
    display_name="Iron Defender",
    searchable_by=["Iron Defender", "Item"],
    subtypes=["Item"],
    collector_number=110,
    set_code="ME5",
    rarity=Rarities.Rare,
    effect=team_types_take_less_next_turn(30, "metal")
)
