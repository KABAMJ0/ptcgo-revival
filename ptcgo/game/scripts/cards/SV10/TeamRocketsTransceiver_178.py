from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, card_named_contains, is_supporter_card

card = ItemCardDef(
    guid="1934bc4e-ceb9-5b0c-a787-b53a024a3dc2",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsTransceiver.Name",
    display_name="Team Rocket's Transceiver",
    searchable_by=["Team Rocket's Transceiver", "Item"],
    subtypes=["Item"],
    collector_number=178,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_supporter_card, card_named_contains("team rocket")), count=1)
)
