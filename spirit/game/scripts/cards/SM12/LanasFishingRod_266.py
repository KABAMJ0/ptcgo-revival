from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import all_of, is_pokemon_card, is_tool_card

card = ItemCardDef(
    guid="c45f0375-1147-5185-bbfc-fc5a9ace97f7",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanasFishingRod.Name",
    display_name="Lana's Fishing Rod",
    searchable_by=["Lana's Fishing Rod", "Item"],
    subtypes=["Item"],
    collector_number=266,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    effect=recover_from_discard(all_of(is_pokemon_card, is_tool_card), count=1, to="deck_shuffle")
)
