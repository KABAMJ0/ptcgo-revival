from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_up_to_draw_pair

card = SupporterCardDef(
    guid="c8485c61-52d1-52ce-b276-6540a31c13a7",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FelicitysDrawing.Name",
    display_name="Felicity's Drawing",
    searchable_by=["Felicity's Drawing", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    effect=discard_up_to_draw_pair(2, None, 3, 4)
)
