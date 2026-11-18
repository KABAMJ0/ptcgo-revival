from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_prizes_face_up

card = ItemCardDef(
    guid="275e04df-b553-5b3b-b793-9a82853fb678",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name",
    display_name="Here Comes Team Rocket!",
    searchable_by=["Here Comes Team Rocket!"],
    subtypes=[],
    collector_number=15,
    set_code="CEL25C",
    rarity=Rarities.Common,
    effect=all_prizes_face_up()
)
