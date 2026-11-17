from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_rule_box_free_pokemon

card = ItemCardDef(
    guid="cfe3652f-f0bb-5537-a894-023145a0c454",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokPad.Name",
    display_name="Poké Pad",
    searchable_by=["Pok\u00e9 Pad", "Item"],
    subtypes=["Item"],
    collector_number=198,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    effect=search_to_hand(is_rule_box_free_pokemon, count=1)
)
