from ptcgo.game.card_effects.trainers import kabu
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="929f74cf-e507-52a4-b677-35b98feedaed",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kabu.Name",
    display_name="Kabu",
    searchable_by=["Kabu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=26,
    set_code="SWSH11TG",
    rarity=Rarities.RareUltra,
    effect=kabu
)
