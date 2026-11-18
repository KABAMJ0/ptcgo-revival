from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_trainer_card, with_discard_cost

card = ItemCardDef(
    guid="402bcc2a-5298-538d-8c97-7103eace63af",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JunkArm.Name",
    display_name="Junk Arm",
    searchable_by=["Junk Arm", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="HGSS4",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(2, recover_from_discard(is_trainer_card, count=1, to="hand", reveal=True))
)
