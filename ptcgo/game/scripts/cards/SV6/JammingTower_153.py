from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import ToolsSuppressedStadiumPassive

card = StadiumCardDef(
    guid="93d010a6-cfc7-5705-8da2-569790f8cbea",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JammingTower.Name",
    display_name="Jamming Tower",
    searchable_by=["Jamming Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=153,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    passive=ToolsSuppressedStadiumPassive()
)
