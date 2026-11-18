from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_may_draw_up_to

card = SupporterCardDef(
    guid="300486c6-3ec5-5def-85b2-26398321ac90",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Erika.Name",
    display_name="Erika",
    searchable_by=["Erika", "Supporter"],
    subtypes=["Supporter"],
    collector_number=191,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=each_may_draw_up_to(3)
)
