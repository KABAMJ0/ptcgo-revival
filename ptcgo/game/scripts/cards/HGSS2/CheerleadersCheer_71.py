from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_opponent_may_draw

card = SupporterCardDef(
    guid="58d94043-fe88-5f04-afdf-a43dad5de773",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CheerleadersCheer.Name",
    display_name="Cheerleader's Cheer",
    searchable_by=["Cheerleader's Cheer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=71,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    effect=draw_then_opponent_may_draw(3, 1)
)
