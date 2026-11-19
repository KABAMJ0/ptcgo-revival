from ptcgo.game.card_effects.trainers import team_types_take_less_next_turn
from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="ad66af6d-0758-5cb9-a2b8-bfdc4ceb73b4",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IronDefender.Name",
    display_name="Iron Defender",
    searchable_by=["Iron Defender", "Item"],
    subtypes=["Item"],
    collector_number=118,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    effect=team_types_take_less_next_turn(30, "metal")
)
