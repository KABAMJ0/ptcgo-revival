from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_prizes_face_up

card = SupporterCardDef(
    guid="f7f04d60-e7bd-5505-afa0-fa7a659625b4",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name",
    display_name="Here Comes Team Rocket!",
    searchable_by=["Here Comes Team Rocket!", "Supporter"],
    subtypes=["Supporter"],
    collector_number=113,
    set_code="XY12",
    rarity=Rarities.RareSecret,
    effect=all_prizes_face_up()
)
