from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="890f1cfc-326c-58c0-96f9-1b959e3af81c",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyStadium.Name",
    display_name="Lucky Stadium",
    searchable_by=["Lucky Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=41,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
