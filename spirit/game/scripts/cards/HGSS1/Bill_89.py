from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="bf8550b2-7ea9-5195-aee6-b5d6773783a2",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bill.Name",
    display_name="Bill",
    searchable_by=["Bill", "Supporter"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=draw_n(2)
)
