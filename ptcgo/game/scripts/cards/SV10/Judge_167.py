from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw

card = SupporterCardDef(
    guid="2059bbd1-a999-530e-a661-9296d85ddee7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=each_player_shuffle_draw(4)
)
