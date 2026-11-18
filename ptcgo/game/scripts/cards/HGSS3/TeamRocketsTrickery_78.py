from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_opponent_discard

card = SupporterCardDef(
    guid="b5d0d560-7be4-563f-81b3-41d43f6f4915",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsTrickery.Name",
    display_name="Team Rocket's Trickery",
    searchable_by=["Team Rocket's Trickery", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="HGSS3",
    rarity=Rarities.Uncommon,
    effect=draw_then_opponent_discard(2, 1)
)
