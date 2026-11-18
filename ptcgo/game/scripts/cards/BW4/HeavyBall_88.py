from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, is_pokemon_card, pokemon_with_retreat_at_least

card = ItemCardDef(
    guid="6e193649-7d79-566c-99c8-8357c5da5d7f",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeavyBall.Name",
    display_name="Heavy Ball",
    searchable_by=["Heavy Ball", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_pokemon_card, pokemon_with_retreat_at_least(3)), count=1)
)
