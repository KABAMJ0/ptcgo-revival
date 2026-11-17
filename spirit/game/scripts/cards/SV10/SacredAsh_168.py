from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="a4f32df7-7b7b-5e3e-af04-cec52991e47d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SacredAsh.Name",
    display_name="Sacred Ash",
    searchable_by=["Sacred Ash", "Item"],
    subtypes=["Item"],
    collector_number=168,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_pokemon_card, count=5, to="deck_shuffle")
)
