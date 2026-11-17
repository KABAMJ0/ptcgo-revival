from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import cure_conditions_effect

card = ItemCardDef(
    guid="42fe7d77-0208-55ed-af0d-799ba83d0b1e",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=cure_conditions_effect(scope="active")
)
