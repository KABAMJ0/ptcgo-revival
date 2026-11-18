from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_to_top

card = SupporterCardDef(
    guid="999af1e2-d460-56b7-b812-18dcfed40236",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mallow.Name",
    display_name="Mallow",
    searchable_by=["Mallow", "Supporter"],
    subtypes=["Supporter"],
    collector_number=127,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=search_to_top(2)
)
