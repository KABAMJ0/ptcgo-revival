from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import heal_all_then_energy_to_hand

card = SupporterCardDef(
    guid="8c003af8-17c8-541f-8c41-373b66e3c92c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WallysCompassion.Name",
    display_name="Wally's Compassion",
    searchable_by=["Wally's Compassion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="ME1",
    rarity=Rarities.Rare,
    effect=heal_all_then_energy_to_hand()
)
