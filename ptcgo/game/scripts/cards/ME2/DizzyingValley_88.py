from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import conditions_survive_evolution_passive

card = StadiumCardDef(
    guid="046a8a33-754f-551e-851e-f23043c5fe88",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DizzyingValley.Name",
    display_name="Dizzying Valley",
    searchable_by=["Dizzying Valley", "Stadium"],
    subtypes=["Stadium"],
    collector_number=88,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    passive=conditions_survive_evolution_passive('Confused')
)
