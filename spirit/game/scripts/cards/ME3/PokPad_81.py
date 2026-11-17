from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_rule_box_free_pokemon

card = ItemCardDef(
    guid="95b97373-1932-515a-b37b-f55affebd47b",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokPad.Name",
    display_name="Poké Pad",
    searchable_by=["Pok\u00e9 Pad", "Item"],
    subtypes=["Item"],
    collector_number=81,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_rule_box_free_pokemon, count=1)
)
