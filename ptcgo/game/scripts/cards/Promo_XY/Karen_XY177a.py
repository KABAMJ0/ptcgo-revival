from ptcgo.game.card_effects.trainers import each_player_shuffle_discard_into_deck, is_pokemon_card
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="cb26bdcb-9b05-54e7-bc13-06b12e1518e7",
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
