from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card, with_discard_cost

card = ItemCardDef(
    guid="9db709ce-a606-5210-9ce4-1f99b8591184",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperiorEnergyRetrieval.Name",
    display_name="Superior Energy Retrieval",
    searchable_by=["Superior Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=103,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(2, recover_from_discard(is_basic_energy_card, count=4, to="hand"))
)
