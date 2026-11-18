from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="1ab3de67-7cea-5db7-b176-8758dfae4ff7",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hau.Name",
    display_name="Hau",
    searchable_by=["Hau", "Supporter"],
    subtypes=["Supporter"],
    collector_number=132,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=draw_n(3)
)
