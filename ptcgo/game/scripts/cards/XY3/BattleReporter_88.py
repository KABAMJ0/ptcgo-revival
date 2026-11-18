from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_until_opponent_hand

card = SupporterCardDef(
    guid="439780a0-3336-5ebe-99b8-8abfba93d6ea",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleReporter.Name",
    display_name="Battle Reporter",
    searchable_by=["Battle Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=draw_until_opponent_hand()
)
