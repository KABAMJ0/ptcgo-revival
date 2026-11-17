from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import each_player_shuffle_draw_per_prize

card = SupporterCardDef(
    guid="2a49c578-3355-55dd-ac29-ada86e642454",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.trainer.N.Name",
    display_name="N",
    searchable_by=["N", "Supporter"],
    subtypes=["Supporter"],
    collector_number=101,
    set_code="ME55C",
    rarity=Rarities.RareUltra,
    effect=each_player_shuffle_draw_per_prize()
)
