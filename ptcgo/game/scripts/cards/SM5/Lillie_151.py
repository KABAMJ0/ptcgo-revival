from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import first_turn_draw_until

card = SupporterCardDef(
    guid="b3b4ff7f-79e7-5f12-8cd6-16476a12de20",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lillie.Name",
    display_name="Lillie",
    searchable_by=["Lillie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=151,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=first_turn_draw_until(6, 8)
)
