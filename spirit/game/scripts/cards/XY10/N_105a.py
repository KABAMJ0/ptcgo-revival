from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import each_player_shuffle_draw_per_prize

card = SupporterCardDef(
    guid="571125f2-970b-5bd1-b4f8-9ddc357f7975",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.N.Name",
    display_name="N",
    searchable_by=["N", "Supporter"],
    subtypes=["Supporter"],
    collector_number=105,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    effect=each_player_shuffle_draw_per_prize()
)
