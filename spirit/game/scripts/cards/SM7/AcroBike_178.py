from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top

card = ItemCardDef(
    guid="f82a585f-6923-591c-91e6-f3bcb85e341e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcroBike.Name",
    display_name="Acro Bike",
    searchable_by=["Acro Bike", "Item"],
    subtypes=["Item"],
    collector_number=178,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    effect=look_at_top(2, take=1)
)
