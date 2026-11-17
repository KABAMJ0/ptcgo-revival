from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n, is_stage_one, opponent_active_is

card = SupporterCardDef(
    guid="2cf723f0-d7bc-5cee-81b0-216b65c1bbcd",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Evelyn.Name",
    display_name="Evelyn",
    searchable_by=["Evelyn", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=draw_n(4), condition=opponent_active_is(is_stage_one)
)
