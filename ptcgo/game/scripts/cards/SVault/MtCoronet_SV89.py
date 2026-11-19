from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of, stadium_ability

card = StadiumCardDef(
    guid="7149eb36-4b7f-5cae-aef6-7507bda35ab6",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MtCoronet.Name",
    display_name="Mt. Coronet",
    searchable_by=["Mt. Coronet", "Stadium"],
    subtypes=["Stadium"],
    collector_number=89,
    set_code="SVault",
    rarity=Rarities.RareSecret,
    ability=stadium_ability('Mt. Coronet', recover_from_discard(basic_energy_of("metal"), count=2, to="hand"))
)
