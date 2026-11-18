from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import gust_then_confuse

card = SupporterCardDef(
    guid="cb74c6bc-caab-5504-b597-1b74be69670f",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LisiasAppeal.Name",
    display_name="Lisia's Appeal",
    searchable_by=["Lisia's Appeal", "Supporter"],
    subtypes=["Supporter"],
    collector_number=234,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=gust_then_confuse()
)
