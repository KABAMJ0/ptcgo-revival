from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card, with_discard_cost

card = ItemCardDef(
    guid="4833b3eb-a467-5992-a592-ce8d20b749cd",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperiorEnergyRetrieval.Name",
    display_name="Superior Energy Retrieval",
    searchable_by=["Superior Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=189,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(2, recover_from_discard(is_basic_energy_card, count=4, to="hand"))
)
