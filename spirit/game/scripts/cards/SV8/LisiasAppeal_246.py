from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gust_then_confuse

card = SupporterCardDef(
    guid="5de96907-7489-5581-b925-9b16fa643150",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LisiasAppeal.Name",
    display_name="Lisia's Appeal",
    searchable_by=["Lisia's Appeal", "Supporter"],
    subtypes=["Supporter"],
    collector_number=246,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=gust_then_confuse()
)
