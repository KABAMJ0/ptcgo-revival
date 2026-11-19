from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import extra_poison_counters

card = StadiumCardDef(
    guid="05a72a5d-eebf-5d02-b466-482575223882",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VirbankCityGym.Name",
    display_name="Virbank City Gym",
    searchable_by=["Virbank City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=126,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    passive=extra_poison_counters(2)
)
