from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_benched_undamaged

card = SupporterCardDef(
    guid="de71ea3b-caf7-5879-adba-979ca5582ede",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisExile.Name",
    display_name="Giovanni's Exile",
    searchable_by=["Giovanni's Exile", "Supporter"],
    subtypes=["Supporter"],
    collector_number=67,
    set_code="HF",
    rarity=Rarities.RareUltra,
    effect=discard_benched_undamaged(2)
)
