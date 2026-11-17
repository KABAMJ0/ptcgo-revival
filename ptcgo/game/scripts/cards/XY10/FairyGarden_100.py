from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import has_energy_of, stadium_no_retreat

card = StadiumCardDef(
    guid="d8690750-dcb9-57ad-95fa-d13f254cef14",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyGarden.Name",
    display_name="Fairy Garden",
    searchable_by=["Fairy Garden", "Stadium"],
    subtypes=["Stadium"],
    collector_number=100,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    passive=stadium_no_retreat(has_energy_of("fairy"))
)
