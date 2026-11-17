from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_energy_to_deck_top

card = SupporterCardDef(
    guid="ea2787c7-5c64-5d32-b47e-6eb3f9a3be41",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamStarGrunt.Name",
    display_name="Team Star Grunt",
    searchable_by=["Team Star Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=242,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=opponent_energy_to_deck_top()
)
