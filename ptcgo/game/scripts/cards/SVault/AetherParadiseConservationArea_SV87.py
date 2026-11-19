from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_type_takes_less

card = StadiumCardDef(
    guid="cbac4046-2668-59a5-b542-d1518ce3bc41",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AetherParadiseConservationArea.Name",
    display_name="Aether Paradise Conservation Area",
    searchable_by=["Aether Paradise Conservation Area", "Stadium"],
    subtypes=["Stadium"],
    collector_number=87,
    set_code="SVault",
    rarity=Rarities.RareSecret,
    passive=stadium_type_takes_less("basic grass and basic lightning pokemon both yours and your opponents take 30 less damage from the opponents attacks after applying weakness and resistance")
)
