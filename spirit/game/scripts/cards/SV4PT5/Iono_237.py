from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import each_player_shuffle_draw_per_prize

card = SupporterCardDef(
    guid="e8570b24-8f6b-545f-8573-238fa1af62eb",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iono.Name",
    display_name="Iono",
    searchable_by=["Iono", "Supporter"],
    subtypes=["Supporter"],
    collector_number=237,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    effect=each_player_shuffle_draw_per_prize()
)
