from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="c8c2dc4b-0221-54d0-8527-000577a20677",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyReturner.Name",
    display_name="Energy Returner",
    searchable_by=["Energy Returner", "Item"],
    subtypes=["Item"],
    collector_number=74,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_basic_energy_card, count=4, to="deck_shuffle", reveal=True)
)
