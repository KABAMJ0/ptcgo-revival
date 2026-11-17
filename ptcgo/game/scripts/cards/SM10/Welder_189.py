from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attach_hand_then_draw, basic_energy_of

card = SupporterCardDef(
    guid="94ab2c0e-e254-5d26-90ae-ad25737d73bd",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Welder.Name",
    display_name="Welder",
    searchable_by=["Welder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=attach_hand_then_draw(basic_energy_of("fire"), count=2, draw=3)
)
