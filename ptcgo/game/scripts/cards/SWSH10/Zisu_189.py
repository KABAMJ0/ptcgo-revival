from ptcgo.game.card_effects.trainers import zisu
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="cad0b9be-03d2-5932-8559-e1f42ff4b198",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Zisu.Name",
    display_name="Zisu",
    searchable_by=["Zisu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    effect=zisu
)
