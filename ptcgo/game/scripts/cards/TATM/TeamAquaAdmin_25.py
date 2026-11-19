from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card, team_aqua_target

card = SupporterCardDef(
    guid="6d4713e6-8061-5b33-b82b-7c09ba157c49",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaAdmin.Name",
    display_name="Team Aqua Admin",
    searchable_by=["Team Aqua Admin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=25,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    effect=attach_from_discard(is_basic_energy_card, count=1,
                        target=lambda target: is_in_active_spot(target)
                        and team_aqua_target(target))
)
