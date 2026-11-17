from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import discard_then_draw

card = SupporterCardDef(
    guid="3f41a19d-8ebf-5746-bb30-ee4ec05fc216",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sophocles.Name",
    display_name="Sophocles",
    searchable_by=["Sophocles", "Supporter"],
    subtypes=["Supporter"],
    collector_number=146,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    effect=discard_then_draw(2, 4)
)
