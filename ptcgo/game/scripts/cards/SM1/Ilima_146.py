from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_flip_draw

card = SupporterCardDef(
    guid="468319ec-3f86-5a21-9543-d9eaaa60dca9",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ilima.Name",
    display_name="Ilima",
    searchable_by=["Ilima", "Supporter"],
    subtypes=["Supporter"],
    collector_number=146,
    set_code="SM1",
    rarity=Rarities.RareUltra,
    effect=each_player_shuffle_flip_draw(6, 3)
)
