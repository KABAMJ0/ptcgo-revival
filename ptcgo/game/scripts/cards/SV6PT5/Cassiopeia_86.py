from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import hand_is_last

card = SupporterCardDef(
    guid="a600233f-9860-5abe-9d3f-c16e356919de",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cassiopeia.Name",
    display_name="Cassiopeia",
    searchable_by=["Cassiopeia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=86,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    effect=search_to_hand(None, count=2), condition=hand_is_last()
)
