from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw

card = SupporterCardDef(
    guid="4e39403d-1e34-5d44-bc87-7b554ad287e1",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=25,
    set_code="SWSH12TG",
    rarity=Rarities.RareUltra,
    effect=each_player_shuffle_draw(4)
)
