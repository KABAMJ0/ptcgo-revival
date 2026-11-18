from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="80c6e8d6-8c02-5900-a975-1b0467a34801",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendsinPaldea.Name",
    display_name="Friends in Paldea",
    searchable_by=["Friends in Paldea", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=draw_n(3)
)
