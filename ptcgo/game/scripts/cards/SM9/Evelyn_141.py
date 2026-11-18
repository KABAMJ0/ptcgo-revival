from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n, is_stage_one, opponent_active_is

card = SupporterCardDef(
    guid="ece2a15c-9062-5922-b9fb-3b4124fcd1fb",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Evelyn.Name",
    display_name="Evelyn",
    searchable_by=["Evelyn", "Supporter"],
    subtypes=["Supporter"],
    collector_number=141,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=draw_n(4), condition=opponent_active_is(is_stage_one)
)
