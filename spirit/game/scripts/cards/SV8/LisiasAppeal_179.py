from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gust_then_confuse

card = SupporterCardDef(
    guid="37c19bf5-83f3-54bb-af42-ef76ab2d407b",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LisiasAppeal.Name",
    display_name="Lisia's Appeal",
    searchable_by=["Lisia's Appeal", "Supporter"],
    subtypes=["Supporter"],
    collector_number=179,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=gust_then_confuse()
)
