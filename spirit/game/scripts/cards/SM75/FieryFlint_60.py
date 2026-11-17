from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import basic_energy_of, with_discard_cost

card = ItemCardDef(
    guid="ac6e3f7b-147d-5e49-93da-042959e0f6e6",
    key="SM75",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieryFlint.Name",
    display_name="Fiery Flint",
    searchable_by=["Fiery Flint", "Item"],
    subtypes=["Item"],
    collector_number=60,
    set_code="SM75",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(2, search_to_hand(basic_energy_of("fire"), count=4))
)
