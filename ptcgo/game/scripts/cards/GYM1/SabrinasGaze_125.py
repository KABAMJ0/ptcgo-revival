from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_count_shuffle_draw

card = ItemCardDef(
    guid="a3834562-2c17-5e08-a84f-ad8648b9f17b",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasGaze.Name",
    display_name="Sabrina's Gaze",
    searchable_by=["Sabrina's Gaze"],
    subtypes=[],
    collector_number=125,
    set_code="GYM1",
    rarity=Rarities.Common,
    effect=each_player_count_shuffle_draw()
)
