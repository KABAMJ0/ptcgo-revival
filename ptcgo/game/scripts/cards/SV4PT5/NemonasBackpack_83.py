from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import card_named_contains

card = ItemCardDef(
    guid="e652c778-7b17-5dd2-8619-a14ea11f5bf1",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NemonasBackpack.Name",
    display_name="Nemona's Backpack",
    searchable_by=["Nemona's Backpack", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(card_named_contains("nemona"), count=2, to="hand", reveal=True)
)
