from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import heal_all_then_energy_to_hand

card = SupporterCardDef(
    guid="5558a073-548d-5de6-bf25-fe6dfa55acfa",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WallysCompassion.Name",
    display_name="Wally's Compassion",
    searchable_by=["Wally's Compassion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=186,
    set_code="ME1",
    rarity=Rarities.Rare,
    effect=heal_all_then_energy_to_hand()
)
