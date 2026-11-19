from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.trainers import basic_energy_of, gx_unlock_for_type, with_discard_cost
from ptcgo.game.card_effects.support_common import search_to_hand


_MISTY_LORELEI = composed(
    search_to_hand(basic_energy_of("water"), count=3, minimum=1, reveal=True,
                   prompt="Choose up to 3 Water Energy cards"),
    then=with_discard_cost(5, gx_unlock_for_type("water")))


card = SupporterCardDef(
    guid="b1b4db87-cec7-5c55-84e9-dc8425cca5ee",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistyLorelei.Name",
    display_name="Misty & Lorelei",
    searchable_by=["Misty & Lorelei", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=199,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=_MISTY_LORELEI,
)
