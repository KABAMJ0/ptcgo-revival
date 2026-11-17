from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import each_player_shuffle_draw_per_prize

card = SupporterCardDef(
    guid="112f827c-1272-5f87-a252-ba756fd77f05",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iono.Name",
    display_name="Iono",
    searchable_by=["Iono", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    effect=each_player_shuffle_draw_per_prize()
)
