from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_energy_opponent

card = SupporterCardDef(
    guid="44b0ed40-5fb4-500d-9ba8-be00d2f93023",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamFlareGrunt.Name",
    display_name="Team Flare Grunt",
    searchable_by=["Team Flare Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=discard_energy_opponent(scope="active")
)
