from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import cure_conditions_effect

card = ItemCardDef(
    guid="df84575c-78ae-544f-bc8d-47879e699761",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=cure_conditions_effect(scope="active")
)
