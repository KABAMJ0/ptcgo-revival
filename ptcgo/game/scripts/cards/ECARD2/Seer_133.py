from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = SupporterCardDef(
    guid="024715b9-f516-53ea-a1f1-42e05ad073af",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Seer.Name",
    display_name="Seer",
    searchable_by=["Seer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    effect=look_at_top(6, take=6, predicate=is_basic_energy_card, minimum=0)
)
