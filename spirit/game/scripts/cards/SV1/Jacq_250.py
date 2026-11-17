from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_evolution_pokemon

card = SupporterCardDef(
    guid="b6b89360-0a80-5f66-ad10-f58f49dcf1bc",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jacq.Name",
    display_name="Jacq",
    searchable_by=["Jacq", "Supporter"],
    subtypes=["Supporter"],
    collector_number=250,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=search_to_hand(is_evolution_pokemon, count=2)
)
