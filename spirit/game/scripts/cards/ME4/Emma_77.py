from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_per_opponent_hand_card, is_pokemon_card

card = SupporterCardDef(
    guid="d7c4d16f-2937-5457-bcf7-b4914a0fd7ea",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Emma.Name",
    display_name="Emma",
    searchable_by=["Emma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    effect=draw_per_opponent_hand_card(predicate=is_pokemon_card, per=1)
)
