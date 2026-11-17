from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import choose_one, is_pokemon_card

card = ItemCardDef(
    guid="8f36a4cb-83a1-56a5-b674-68bc025c73db",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueStretcher.Name",
    display_name="Rescue Stretcher",
    searchable_by=["Rescue Stretcher", "Item"],
    subtypes=["Item"],
    collector_number=130,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=choose_one([("Put a Pokémon from your discard pile into your hand", recover_from_discard(is_pokemon_card, count=1, to="hand")), ("Shuffle 3 Pokémon from your discard pile into your deck", recover_from_discard(is_pokemon_card, count=3, to="deck_shuffle"))])
)
