from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="b9049447-56cf-5789-a078-177bfe40243d",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MomsKindness.Name",
    display_name="Mom's Kindness",
    searchable_by=["Mom's Kindness", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=draw_n(2)
)
