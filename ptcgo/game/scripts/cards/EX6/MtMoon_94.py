from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.passives_common import ability_lock_passive
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="71fb1a9d-63cb-5cee-af3c-cc7c8202a493",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MtMoon.Name",
    display_name="Mt. Moon",
    searchable_by=["Mt. Moon", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    passive=ability_lock_passive(lambda p, c: p.get_attribute(AttrID.HP, 0) < 70)
)
