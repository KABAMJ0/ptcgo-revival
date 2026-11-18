from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import prevent_damage_when


def _benched_target(calc, carrier):
    return not calc.to_active

card = StadiumCardDef(
    guid="c6c72ca5-6e31-5b00-a99d-cee00ca1c061",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MountainRing.Name",
    display_name="Mountain Ring",
    searchable_by=["Mountain Ring", "Stadium"],
    subtypes=["Stadium"],
    collector_number=97,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    passive=prevent_damage_when(_benched_target, any_side=True)
)
