from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="c44dca6a-27da-56f3-89bc-3e49607496ea",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=94,
    set_code="BW10",
    rarity=Rarities.Rare,
    effect=search_to_hand(is_pokemon_card, count=1)
)
