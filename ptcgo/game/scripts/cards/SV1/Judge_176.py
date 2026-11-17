from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw

card = SupporterCardDef(
    guid="011a4419-840d-5a73-ad34-450491bb8c59",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=each_player_shuffle_draw(4)
)
