from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import pokemon_of

card = SupporterCardDef(
    guid="df800b75-141c-52e4-bfb7-039b578a4057",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Winona.Name",
    display_name="Winona",
    searchable_by=["Winona", "Supporter"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="XY6",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(pokemon_of("colorless"), count=3)
)
