from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_count_shuffle_draw

card = SupporterCardDef(
    guid="ce73b5ae-ab8e-5a5e-857e-2e9d2280e2e0",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wicke.Name",
    display_name="Wicke",
    searchable_by=["Wicke", "Supporter"],
    subtypes=["Supporter"],
    collector_number=147,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    effect=each_player_count_shuffle_draw()
)
