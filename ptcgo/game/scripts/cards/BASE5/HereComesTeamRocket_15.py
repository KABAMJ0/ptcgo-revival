from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_prizes_face_up

card = ItemCardDef(
    guid="c1823d45-d150-54bc-ac26-4dcedad8870d",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name",
    display_name="Here Comes Team Rocket!",
    searchable_by=["Here Comes Team Rocket!"],
    subtypes=[],
    collector_number=15,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    effect=all_prizes_face_up()
)
