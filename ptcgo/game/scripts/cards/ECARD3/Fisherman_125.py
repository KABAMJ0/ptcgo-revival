from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = SupporterCardDef(
    guid="f1937dc1-34e8-52f3-8e0d-16cf1ab528a6",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name",
    display_name="Fisherman",
    searchable_by=["Fisherman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=125,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_basic_energy_card, count=4, to="hand")
)
