from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="fefe6c30-c549-57f9-bf6f-2a0f948ec462",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SacredAsh.Name",
    display_name="Sacred Ash",
    searchable_by=["Sacred Ash", "Item"],
    subtypes=["Item"],
    collector_number=115,
    set_code="ME3",
    rarity=Rarities.Rare,
    effect=recover_from_discard(is_pokemon_card, count=5, to="deck_shuffle")
)
