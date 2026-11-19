from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import bench_capacity_passive

card = StadiumCardDef(
    guid="ca0234f1-1d6c-5034-8e96-3b1c06d62344",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NarrowGym.Name",
    display_name="Narrow Gym",
    searchable_by=["Narrow Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=124,
    set_code="GYM1",
    rarity=Rarities.Common,
    passive=bench_capacity_passive(4, protects='each', trim_to='hand')
)
