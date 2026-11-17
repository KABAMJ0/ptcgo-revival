from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="7de8acfb-8841-573c-95a5-261fad9de36c",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nemona.Name",
    display_name="Nemona",
    searchable_by=["Nemona", "Supporter"],
    subtypes=["Supporter"],
    collector_number=238,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    effect=draw_n(3)
)
