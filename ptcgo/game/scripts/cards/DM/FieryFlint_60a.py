from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import basic_energy_of, with_discard_cost

card = ItemCardDef(
    guid="11a64d81-279d-50cb-b505-2c853702f65c",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieryFlint.Name",
    display_name="Fiery Flint",
    searchable_by=["Fiery Flint", "Item"],
    subtypes=["Item"],
    collector_number=60,
    set_code="DM",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(2, search_to_hand(basic_energy_of("fire"), count=4))
)
