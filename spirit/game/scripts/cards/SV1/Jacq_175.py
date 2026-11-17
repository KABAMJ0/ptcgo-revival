from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_evolution_pokemon

card = SupporterCardDef(
    guid="d49d2326-52be-5d28-8d2b-60490845d287",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jacq.Name",
    display_name="Jacq",
    searchable_by=["Jacq", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_evolution_pokemon, count=2)
)
