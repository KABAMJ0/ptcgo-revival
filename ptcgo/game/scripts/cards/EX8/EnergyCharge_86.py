from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import if_heads, is_basic_energy_card
from ptcgo.game.card_effects.support_common import recover_from_discard


_ENERGY_CHARGE = if_heads(recover_from_discard(is_basic_energy_card, count=2, minimum=0,
                     reveal=True, to="deck_shuffle"))


card = ItemCardDef(
    guid="f19d4531-d8d0-579d-a216-292a4d5510a9",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyCharge.Name",
    display_name="Energy Charge",
    searchable_by=["Energy Charge", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    effect=_ENERGY_CHARGE
)
