from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card, with_discard_cost

card = ItemCardDef(
    guid="ebf827cc-87f7-5f88-8c90-b9cef15f43c9",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperiorEnergyRetrieval.Name",
    display_name="Superior Energy Retrieval",
    searchable_by=["Superior Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=277,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=with_discard_cost(2, recover_from_discard(is_basic_energy_card, count=4, to="hand"))
)
