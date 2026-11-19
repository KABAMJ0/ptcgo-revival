from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_type_takes_less

card = StadiumCardDef(
    guid="40604de2-33bc-557c-bcbc-b23665cbb5e8",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullMetalLab.Name",
    display_name="Full Metal Lab",
    searchable_by=["Full Metal Lab", "Stadium"],
    subtypes=["Stadium"],
    collector_number=148,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    passive=stadium_type_takes_less('metal pokemon both yours and your opponents take 30 less damage from attacks from the opponents pokemon after applying weakness and resistance put it into the active spot and discard it if another stadium comes into play')
)
