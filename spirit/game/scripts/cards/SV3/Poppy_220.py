from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card, move_basic_energy

card = SupporterCardDef(
    guid="81b27881-4508-575b-9b1c-6bd12d844cd2",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Poppy.Name",
    display_name="Poppy",
    searchable_by=["Poppy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=220,
    set_code="SV3",
    rarity=Rarities.Rare,
    effect=move_basic_energy(predicate=is_basic_energy_card, count=2)
)
