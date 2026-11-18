from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import choose_one, is_pokemon_card

card = ItemCardDef(
    guid="653e090e-d8be-5477-b622-30f83c5e6d06",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueStretcher.Name",
    display_name="Rescue Stretcher",
    searchable_by=["Rescue Stretcher", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    effect=choose_one([("Put a Pokémon from your discard pile into your hand", recover_from_discard(is_pokemon_card, count=1, to="hand")), ("Shuffle 3 Pokémon from your discard pile into your deck", recover_from_discard(is_pokemon_card, count=3, to="deck_shuffle"))])
)
