from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_flip_bonus

card = SupporterCardDef(
    guid="824cd96a-2209-5375-8ffb-c0694a5407ba",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BugCatcher.Name",
    display_name="Bug Catcher",
    searchable_by=["Bug Catcher", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=draw_then_flip_bonus(2, 2, 1)
)
