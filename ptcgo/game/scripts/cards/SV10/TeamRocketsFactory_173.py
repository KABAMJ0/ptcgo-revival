from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_draw_if_named_supporter

card = StadiumCardDef(
    guid="57d502b1-8f81-5212-a009-a321067ea92d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsFactory.Name",
    display_name="Team Rocket's Factory",
    searchable_by=["Team Rocket's Factory", "Stadium"],
    subtypes=["Stadium"],
    collector_number=173,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=stadium_draw_if_named_supporter("team rocket", 2)
)
