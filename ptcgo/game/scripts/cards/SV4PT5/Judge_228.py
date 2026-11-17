from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw

card = SupporterCardDef(
    guid="535a8cc0-af91-596f-9aa3-f51157f0c065",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=228,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    effect=each_player_shuffle_draw(4)
)
