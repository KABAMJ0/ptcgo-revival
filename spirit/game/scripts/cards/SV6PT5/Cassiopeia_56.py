from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import hand_is_last

card = SupporterCardDef(
    guid="6f7f0ce2-0e9d-5a38-97ff-94359cf21074",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cassiopeia.Name",
    display_name="Cassiopeia",
    searchable_by=["Cassiopeia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=56,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(None, count=2), condition=hand_is_last()
)
