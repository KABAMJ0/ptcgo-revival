from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_item_card, pokemon_of

card = SupporterCardDef(
    guid="0a884062-fb4e-5970-ba25-7ae0834d6dd3",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Korrina.Name",
    display_name="Korrina",
    searchable_by=["Korrina", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(all_of(pokemon_of("fighting"), is_item_card), count=1)
)
