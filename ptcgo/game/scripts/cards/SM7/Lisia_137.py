from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_prism_star

card = SupporterCardDef(
    guid="170666de-07f5-5edf-9be1-f084cf6c13d1",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lisia.Name",
    display_name="Lisia",
    searchable_by=["Lisia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_prism_star, count=2)
)
