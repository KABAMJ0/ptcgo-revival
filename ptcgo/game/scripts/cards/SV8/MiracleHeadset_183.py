from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="263e498a-542f-57ed-9fe5-193be15d1b63",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleHeadset.Name",
    display_name="Miracle Headset",
    searchable_by=["Miracle Headset", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=183,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=recover_from_discard(is_supporter_card, count=2, to="hand")
)
