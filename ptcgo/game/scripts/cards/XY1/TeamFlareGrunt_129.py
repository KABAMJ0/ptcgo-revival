from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent

card = SupporterCardDef(
    guid="c91261c9-93cc-515f-990f-575006157dfc",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamFlareGrunt.Name",
    display_name="Team Flare Grunt",
    searchable_by=["Team Flare Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=129,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=discard_energy_opponent(scope="active")
)
