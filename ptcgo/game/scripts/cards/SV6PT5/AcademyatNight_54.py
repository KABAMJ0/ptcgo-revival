from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_card_to_top, stadium_ability

card = StadiumCardDef(
    guid="c5538035-2fd0-5cdc-b85e-64955907d873",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcademyatNight.Name",
    display_name="Academy at Night",
    searchable_by=["Academy at Night", "Stadium"],
    subtypes=["Stadium"],
    collector_number=54,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Academy at Night', hand_card_to_top())
)
