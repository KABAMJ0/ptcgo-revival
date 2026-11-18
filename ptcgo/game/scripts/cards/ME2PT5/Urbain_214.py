from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="7fd00d63-eee8-5c38-9c28-8f75ad044e1b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Urbain.Name",
    display_name="Urbain",
    searchable_by=["Urbain", "Supporter"],
    subtypes=["Supporter"],
    collector_number=214,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=draw_n(3)
)
