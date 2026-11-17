from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import cure_conditions_effect

card = ItemCardDef(
    guid="be9a1491-756a-559c-aec4-c46fd9aa3d17",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DoubleFullHeal.Name",
    display_name="Double Full Heal",
    searchable_by=["Double Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=76,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    effect=cure_conditions_effect(scope="each_own")
)
