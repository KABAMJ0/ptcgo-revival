from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_per_opponent_hand_card, is_pokemon_card

card = SupporterCardDef(
    guid="5421d795-11cf-5aae-a01c-a22f660ef608",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Emma.Name",
    display_name="Emma",
    searchable_by=["Emma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=107,
    set_code="ME4",
    rarity=Rarities.Rare,
    effect=draw_per_opponent_hand_card(predicate=is_pokemon_card, per=1)
)
