from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attach_hand_then_draw, basic_energy_of

card = SupporterCardDef(
    guid="fc29c62f-0299-51d5-8585-522057babbe8",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Welder.Name",
    display_name="Welder",
    searchable_by=["Welder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=214,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    effect=attach_hand_then_draw(basic_energy_of("fire"), count=2, draw=3)
)
