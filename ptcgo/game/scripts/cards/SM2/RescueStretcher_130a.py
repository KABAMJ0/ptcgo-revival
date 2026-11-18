from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import choose_one, is_pokemon_card

card = ItemCardDef(
    guid="223ea9a6-01e8-5520-9ed8-ba868ef81245",
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
