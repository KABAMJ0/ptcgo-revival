from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card, move_basic_energy

card = SupporterCardDef(
    guid="41c54a0b-0a02-5c43-ae3b-2a78776af5b0",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Poppy.Name",
    display_name="Poppy",
    searchable_by=["Poppy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=227,
    set_code="SV3",
    rarity=Rarities.Rare,
    effect=move_basic_energy(predicate=is_basic_energy_card, count=2)
)
