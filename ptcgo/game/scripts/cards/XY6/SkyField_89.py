from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.card_effects.passives_common import bench_capacity_passive
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="81f06034-e5c6-5c67-b544-9600c2591bfe",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkyField.Name",
    display_name="Sky Field",
    searchable_by=["Sky Field", "Stadium"],
    subtypes=["Stadium"],
    collector_number=89,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    passive=bench_capacity_passive(8, mode="raise")
)
