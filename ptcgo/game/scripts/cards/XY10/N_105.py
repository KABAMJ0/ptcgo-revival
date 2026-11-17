from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw_per_prize

card = SupporterCardDef(
    guid="86272063-ca7a-53d5-a076-1c42657e95bc",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.N.Name",
    display_name="N",
    searchable_by=["N", "Supporter"],
    subtypes=["Supporter"],
    collector_number=105,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=each_player_shuffle_draw_per_prize()
)
