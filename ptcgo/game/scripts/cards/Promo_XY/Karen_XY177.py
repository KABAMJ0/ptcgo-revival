from ptcgo.game.card_effects.trainers import each_player_shuffle_discard_into_deck, is_pokemon_card
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="c84a5de9-5c43-5ec4-997e-5c6dfb670cf0",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Karen.Name",
    display_name="Karen",
    searchable_by=["Karen", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    effect=each_player_shuffle_discard_into_deck(predicate=lambda card, player_id: is_pokemon_card(card))
)
