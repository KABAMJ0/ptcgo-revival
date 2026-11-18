from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, move_basic_energy

card = SupporterCardDef(
    guid="90a64659-080d-5a8b-827a-cad7ebd89506",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Poppy.Name",
    display_name="Poppy",
    searchable_by=["Poppy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=193,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    effect=move_basic_energy(predicate=is_basic_energy_card, count=2)
)
