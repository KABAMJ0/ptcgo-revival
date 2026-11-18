from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of, stadium_ability

card = StadiumCardDef(
    guid="a5e0c70a-ae34-542b-bbab-8a774b4b9348",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MtCoronet.Name",
    display_name="Mt. Coronet",
    searchable_by=["Mt. Coronet", "Stadium"],
    subtypes=["Stadium"],
    collector_number=130,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Mt. Coronet', recover_from_discard(basic_energy_of("metal"), count=2, to="hand"))
)
