from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import each_player_shuffle_draw_per_prize

card = SupporterCardDef(
    guid="af3cefab-7d0b-5df3-a403-f80dec3701c3",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iono.Name",
    display_name="Iono",
    searchable_by=["Iono", "Supporter"],
    subtypes=["Supporter"],
    collector_number=185,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    effect=each_player_shuffle_draw_per_prize()
)
