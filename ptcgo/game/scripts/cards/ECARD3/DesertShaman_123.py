from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw_up_to

card = SupporterCardDef(
    guid="56a14c5e-dbbf-5d20-b874-4bba005c042b",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DesertShaman.Name",
    display_name="Desert Shaman",
    searchable_by=["Desert Shaman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=each_player_shuffle_draw_up_to(4)
)
