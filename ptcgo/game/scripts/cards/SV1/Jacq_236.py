from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_evolution_pokemon

card = SupporterCardDef(
    guid="88b57340-df11-505a-b68c-bce736ed5517",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jacq.Name",
    display_name="Jacq",
    searchable_by=["Jacq", "Supporter"],
    subtypes=["Supporter"],
    collector_number=236,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=search_to_hand(is_evolution_pokemon, count=2)
)
