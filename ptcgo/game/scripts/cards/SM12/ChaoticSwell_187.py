from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import voids_stadium_play

card = StadiumCardDef(
    guid="53ff5d70-7635-5aad-b190-be61c579151d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChaoticSwell.Name",
    display_name="Chaotic Swell",
    searchable_by=["Chaotic Swell", "Stadium"],
    subtypes=["Stadium"],
    collector_number=187,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    passive=voids_stadium_play()
)
