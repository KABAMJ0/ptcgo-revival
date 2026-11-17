from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import discard_then_draw

card = SupporterCardDef(
    guid="2ffa760e-0269-5e53-bf88-8108384c4f88",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sophocles.Name",
    display_name="Sophocles",
    searchable_by=["Sophocles", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=discard_then_draw(2, 4)
)
