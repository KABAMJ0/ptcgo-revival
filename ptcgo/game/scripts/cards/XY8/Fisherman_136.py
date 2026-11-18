from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = SupporterCardDef(
    guid="3e6a37da-7286-5304-b7d5-41a369fa2e9a",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name",
    display_name="Fisherman",
    searchable_by=["Fisherman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=136,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_basic_energy_card, count=4, to="hand")
)
