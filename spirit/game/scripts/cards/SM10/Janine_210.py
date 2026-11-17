from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top

card = SupporterCardDef(
    guid="05f5918c-1289-521e-88d2-2d83ec6486ad",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Janine.Name",
    display_name="Janine",
    searchable_by=["Janine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=210,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    effect=look_at_top(4, take=2)
)
