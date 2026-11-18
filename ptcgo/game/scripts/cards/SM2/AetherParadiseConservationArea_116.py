from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_type_takes_less

card = StadiumCardDef(
    guid="9b047b0c-08d7-59a2-9c03-dcf509f6f918",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AetherParadiseConservationArea.Name",
    display_name="Aether Paradise Conservation Area",
    searchable_by=["Aether Paradise Conservation Area", "Stadium"],
    subtypes=["Stadium"],
    collector_number=116,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    passive=stadium_type_takes_less("basic grass and basic lightning pokemon both yours and your opponents take 30 less damage from the opponents attacks after applying weakness and resistance")
)
