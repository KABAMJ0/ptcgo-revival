from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import all_of, is_pokemon_card, is_tool_card

card = ItemCardDef(
    guid="ce1ff911-03ad-5070-9ccf-16c16af8f7a0",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanasFishingRod.Name",
    display_name="Lana's Fishing Rod",
    searchable_by=["Lana's Fishing Rod", "Item"],
    subtypes=["Item"],
    collector_number=195,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(all_of(is_pokemon_card, is_tool_card), count=1, to="deck_shuffle")
)
