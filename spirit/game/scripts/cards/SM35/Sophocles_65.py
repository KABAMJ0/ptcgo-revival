from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import discard_then_draw

card = SupporterCardDef(
    guid="121d7b5b-2df7-54ef-b717-d18bb0806535",
    key="SM35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sophocles.Name",
    display_name="Sophocles",
    searchable_by=["Sophocles", "Supporter"],
    subtypes=["Supporter"],
    collector_number=65,
    set_code="SM35",
    rarity=Rarities.Uncommon,
    effect=discard_then_draw(2, 4)
)
