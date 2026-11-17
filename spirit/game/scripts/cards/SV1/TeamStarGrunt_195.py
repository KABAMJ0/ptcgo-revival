from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_energy_to_deck_top

card = SupporterCardDef(
    guid="ead80a62-5434-5b9b-a67f-7fe883f93502",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamStarGrunt.Name",
    display_name="Team Star Grunt",
    searchable_by=["Team Star Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=195,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=opponent_energy_to_deck_top()
)
