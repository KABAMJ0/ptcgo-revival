from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_energy_to_deck_top

card = SupporterCardDef(
    guid="11c31fd9-0575-5b39-9b68-b0b201bb5ca9",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamStarGrunt.Name",
    display_name="Team Star Grunt",
    searchable_by=["Team Star Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=195,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    effect=opponent_energy_to_deck_top()
)
