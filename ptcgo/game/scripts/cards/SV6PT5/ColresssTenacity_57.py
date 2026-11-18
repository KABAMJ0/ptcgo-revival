from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, is_energy_card, is_stadium_card

card = SupporterCardDef(
    guid="6e74d7d9-e296-5de3-8cae-840062e31669",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ColresssTenacity.Name",
    display_name="Colress's Tenacity",
    searchable_by=["Colress's Tenacity", "Supporter"],
    subtypes=["Supporter"],
    collector_number=57,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_stadium_card, is_energy_card), count=1)
)
