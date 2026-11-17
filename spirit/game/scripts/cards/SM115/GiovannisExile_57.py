from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_benched_undamaged

card = SupporterCardDef(
    guid="b81603de-d01a-550f-b459-e432994f862a",
    key="SM115",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisExile.Name",
    display_name="Giovanni's Exile",
    searchable_by=["Giovanni's Exile", "Supporter"],
    subtypes=["Supporter"],
    collector_number=57,
    set_code="SM115",
    rarity=Rarities.Uncommon,
    effect=discard_benched_undamaged(2)
)
