from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = SupporterCardDef(
    guid="1ed0d286-2d5e-55d5-a48d-3a5dab10626e",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name",
    display_name="Fisherman",
    searchable_by=["Fisherman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="SVault",
    rarity=Rarities.RareUltra,
    effect=recover_from_discard(is_basic_energy_card, count=4, to="hand")
)
