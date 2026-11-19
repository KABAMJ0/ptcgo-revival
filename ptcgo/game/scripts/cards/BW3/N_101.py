from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw_per_prize

card = SupporterCardDef(
    guid="4a1cbb25-f185-595d-813d-edc372b9adc6",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.N.Name",
    display_name="N",
    searchable_by=["N", "Supporter"],
    subtypes=["Supporter"],
    collector_number=101,
    set_code="BW3",
    rarity=Rarities.RareUltra,
    effect=each_player_shuffle_draw_per_prize()
)
