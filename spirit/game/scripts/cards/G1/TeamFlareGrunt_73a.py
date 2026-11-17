from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_energy_opponent

card = SupporterCardDef(
    guid="17dd5516-3efc-5923-b693-7b8f83aaef09",
    key="G1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamFlareGrunt.Name",
    display_name="Team Flare Grunt",
    searchable_by=["Team Flare Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="G1",
    rarity=Rarities.RareUltra,
    effect=discard_energy_opponent(scope="active")
)
