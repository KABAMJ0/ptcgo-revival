from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_ability, if_heads, any_of, basic_energy_of, is_metal_energy_card
from ptcgo.game.card_effects.support_common import recover_from_discard

_CONDUCTIVE_QUARRY_RECOVER = if_heads(
    recover_from_discard(
        any_of(basic_energy_of("lightning"), basic_energy_of("metal"),
               is_metal_energy_card),
        1, reveal=True))


card = StadiumCardDef(
    guid="3c15ea4d-c419-5041-a60d-a8a453342795",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ConductiveQuarry.Name",
    display_name="Conductive Quarry",
    searchable_by=["Conductive Quarry", "Stadium"],
    subtypes=["Stadium"],
    collector_number=82,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Conductive Quarry", _CONDUCTIVE_QUARRY_RECOVER),
)
