from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw

card = SupporterCardDef(
    guid="4cffeac9-bfc2-5f59-87b7-dabc51af68f9",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=143,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=each_player_shuffle_draw(4)
)
