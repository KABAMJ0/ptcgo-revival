from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="9c73a8ee-37f3-5087-b57f-8e998f8cada7",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cheren.Name",
    display_name="Cheren",
    searchable_by=["Cheren", "Supporter"],
    subtypes=["Supporter"],
    collector_number=81,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    effect=draw_n(3)
)
