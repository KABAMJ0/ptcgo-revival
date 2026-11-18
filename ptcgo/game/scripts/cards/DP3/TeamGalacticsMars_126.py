from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_opponent_card_to_bottom

card = SupporterCardDef(
    guid="3ebd3900-f6d2-51bb-a8ce-032dbdf3ffdb",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamGalacticsMars.Name",
    display_name="Team Galactic's Mars",
    searchable_by=["Team Galactic's Mars", "Supporter"],
    subtypes=["Supporter"],
    collector_number=126,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=draw_then_opponent_card_to_bottom(2, 1)
)
