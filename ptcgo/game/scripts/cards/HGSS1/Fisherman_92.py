from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = SupporterCardDef(
    guid="7c662d25-c2c8-5dca-bbdb-16ac54a2f664",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name",
    display_name="Fisherman",
    searchable_by=["Fisherman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=92,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_basic_energy_card, count=4, to="hand", reveal=True)
)
