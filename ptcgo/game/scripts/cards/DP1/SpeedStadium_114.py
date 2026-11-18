from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_until_tails_draw, stadium_ability

card = StadiumCardDef(
    guid="ccc3ee1d-ce38-59cd-a7e3-cd22c9467086",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpeedStadium.Name",
    display_name="Speed Stadium",
    searchable_by=["Speed Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=114,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Speed Stadium', flip_until_tails_draw(1))
)
