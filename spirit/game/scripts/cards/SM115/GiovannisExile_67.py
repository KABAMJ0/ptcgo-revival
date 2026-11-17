from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_benched_undamaged

card = SupporterCardDef(
    guid="de71ea3b-caf7-5879-adba-979ca5582ede",
    key="SM115",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisExile.Name",
    display_name="Giovanni's Exile",
    searchable_by=["Giovanni's Exile", "Supporter"],
    subtypes=["Supporter"],
    collector_number=67,
    set_code="SM115",
    rarity=Rarities.RareUltra,
    effect=discard_benched_undamaged(2)
)
