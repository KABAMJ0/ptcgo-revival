from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card, knocked_out_last_turn

card = ItemCardDef(
    guid="aefd08c6-46e8-5f44-bad9-b34a691eefce",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LetterofEncouragement.Name",
    display_name="Letter of Encouragement",
    searchable_by=["Letter of Encouragement", "Item"],
    subtypes=["Item"],
    collector_number=189,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_basic_energy_card, count=3), condition=knocked_out_last_turn()
)
