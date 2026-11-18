from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of, stadium_ability

card = StadiumCardDef(
    guid="45f8a462-29d2-58b1-a8dc-79f1918a9c70",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Levincia.Name",
    display_name="Levincia",
    searchable_by=["Levincia", "Stadium"],
    subtypes=["Stadium"],
    collector_number=150,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Levincia', recover_from_discard(basic_energy_of("lightning"), count=2, to="hand"))
)
