from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw_per_prize

card = SupporterCardDef(
    guid="e24a4cb0-5222-5d39-a9d6-ba0545d44c8f",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iono.Name",
    display_name="Iono",
    searchable_by=["Iono", "Supporter"],
    subtypes=["Supporter"],
    collector_number=254,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=each_player_shuffle_draw_per_prize()
)
