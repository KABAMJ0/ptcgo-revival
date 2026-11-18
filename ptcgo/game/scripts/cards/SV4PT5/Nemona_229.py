from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="22af6f04-687d-57d3-92a7-4c5a63479aea",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nemona.Name",
    display_name="Nemona",
    searchable_by=["Nemona", "Supporter"],
    subtypes=["Supporter"],
    collector_number=229,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    effect=draw_n(3)
)
