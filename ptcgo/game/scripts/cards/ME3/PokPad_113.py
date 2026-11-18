from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_rule_box_free_pokemon

card = ItemCardDef(
    guid="92483030-6a38-53bf-9c05-66c1e683c53b",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokPad.Name",
    display_name="Poké Pad",
    searchable_by=["Pok\u00e9 Pad", "Item"],
    subtypes=["Item"],
    collector_number=113,
    set_code="ME3",
    rarity=Rarities.Rare,
    effect=search_to_hand(is_rule_box_free_pokemon, count=1)
)
