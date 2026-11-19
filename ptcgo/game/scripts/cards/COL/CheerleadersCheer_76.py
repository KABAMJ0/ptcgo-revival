from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_opponent_may_draw

card = SupporterCardDef(
    guid="067e31c9-9eb8-5607-ba73-8bc908299d5d",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CheerleadersCheer.Name",
    display_name="Cheerleader's Cheer",
    searchable_by=["Cheerleader's Cheer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=76,
    set_code="COL",
    rarity=Rarities.Uncommon,
    effect=draw_then_opponent_may_draw(3, 1)
)
