from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="969544e8-7930-5b65-8bd8-5549fa17c61a",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=153,
    set_code="SV5",
    rarity=Rarities.Rare,
    effect=search_to_hand(is_pokemon_card, count=1)
)
