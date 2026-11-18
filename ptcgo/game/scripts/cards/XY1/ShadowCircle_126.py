from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_no_weakness, has_energy_of

card = StadiumCardDef(
    guid="afd45c1b-a248-5969-b353-fdc1f4061b38",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShadowCircle.Name",
    display_name="Shadow Circle",
    searchable_by=["Shadow Circle", "Stadium"],
    subtypes=["Stadium"],
    collector_number=126,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    passive=stadium_no_weakness(has_energy_of("darkness"))
)
