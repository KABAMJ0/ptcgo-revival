from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_draw_if_named_supporter

card = StadiumCardDef(
    guid="28226147-9b47-5f02-bc57-fb9f7cffd12f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsFactory.Name",
    display_name="Team Rocket's Factory",
    searchable_by=["Team Rocket's Factory", "Stadium"],
    subtypes=["Stadium"],
    collector_number=203,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=stadium_draw_if_named_supporter("team rocket", 2)
)
