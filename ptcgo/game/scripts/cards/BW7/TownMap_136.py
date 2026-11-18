from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import prize_face_up

card = ItemCardDef(
    guid="05396c65-9f46-518e-a9db-9173574366f0",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TownMap.Name",
    display_name="Town Map",
    searchable_by=["Town Map", "Item"],
    subtypes=["Item"],
    collector_number=136,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    effect=prize_face_up()
)
