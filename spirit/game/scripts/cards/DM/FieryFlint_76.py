from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import basic_energy_of, with_discard_cost

card = ItemCardDef(
    guid="a3ce3b39-962a-56d9-84b7-72d1dcfdea2a",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieryFlint.Name",
    display_name="Fiery Flint",
    searchable_by=["Fiery Flint", "Item"],
    subtypes=["Item"],
    collector_number=76,
    set_code="DM",
    rarity=Rarities.RareSecret,
    effect=with_discard_cost(2, search_to_hand(basic_energy_of("fire"), count=4))
)
