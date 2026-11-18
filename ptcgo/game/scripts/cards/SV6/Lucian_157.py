from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_flip_draw

card = SupporterCardDef(
    guid="5e00e3ac-c8b5-5203-87fd-4dfb7909cc65",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lucian.Name",
    display_name="Lucian",
    searchable_by=["Lucian", "Supporter"],
    subtypes=["Supporter"],
    collector_number=157,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    effect=each_player_shuffle_flip_draw(6, 3)
)
