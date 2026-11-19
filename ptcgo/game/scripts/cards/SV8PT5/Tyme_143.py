from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import guess_card_hp

card = SupporterCardDef(
    guid="1624bb3e-ec59-5ef2-940a-fdb3db2a5324",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tyme.Name",
    display_name="Tyme",
    searchable_by=["Tyme", "Supporter"],
    subtypes=["Supporter"],
    collector_number=143,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=guess_card_hp(4)
)
