from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import has_energy_of, stadium_no_retreat

card = StadiumCardDef(
    guid="3795d02e-1bd6-5a7f-8d79-c1b2548cd42d",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyGarden.Name",
    display_name="Fairy Garden",
    searchable_by=["Fairy Garden", "Stadium"],
    subtypes=["Stadium"],
    collector_number=117,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    passive=stadium_no_retreat(has_energy_of("fairy"))
)
