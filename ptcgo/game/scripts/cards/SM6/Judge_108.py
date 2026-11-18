from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw

card = SupporterCardDef(
    guid="844bb265-b3fe-51da-a98b-c43786c85389",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    effect=each_player_shuffle_draw(4)
)
