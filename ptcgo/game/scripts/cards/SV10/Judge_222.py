from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw

card = SupporterCardDef(
    guid="7b2c4b16-9492-53db-9952-acd66d076982",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=222,
    set_code="SV10",
    rarity=Rarities.Rare,
    effect=each_player_shuffle_draw(4)
)
