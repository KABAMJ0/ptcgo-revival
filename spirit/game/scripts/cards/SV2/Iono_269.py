from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import each_player_shuffle_draw_per_prize

card = SupporterCardDef(
    guid="fdcf4db7-ef52-508e-a48a-da13938a466f",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iono.Name",
    display_name="Iono",
    searchable_by=["Iono", "Supporter"],
    subtypes=["Supporter"],
    collector_number=269,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=each_player_shuffle_draw_per_prize()
)
