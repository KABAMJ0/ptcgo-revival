from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import any_of, is_stadium_card, is_supporter_card

card = SupporterCardDef(
    guid="426d434b-96f3-56a4-9227-e7ef2e735d67",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RelicHunter.Name",
    display_name="Relic Hunter",
    searchable_by=["Relic Hunter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(any_of(is_supporter_card, is_stadium_card), count=2)
)
