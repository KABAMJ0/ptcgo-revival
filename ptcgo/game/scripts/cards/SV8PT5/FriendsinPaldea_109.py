from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="599681c6-6058-565b-8daa-5ae181b09a1c",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendsinPaldea.Name",
    display_name="Friends in Paldea",
    searchable_by=["Friends in Paldea", "Supporter"],
    subtypes=["Supporter"],
    collector_number=109,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    effect=draw_n(3)
)
