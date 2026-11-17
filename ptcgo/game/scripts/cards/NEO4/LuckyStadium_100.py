from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n, if_heads, stadium_ability

card = StadiumCardDef(
    guid="53558e57-a4d1-5d49-bf3f-af31b2fa8a88",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyStadium.Name",
    display_name="Lucky Stadium",
    searchable_by=["Lucky Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=100,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Lucky Stadium', if_heads(draw_n(1)))
)
