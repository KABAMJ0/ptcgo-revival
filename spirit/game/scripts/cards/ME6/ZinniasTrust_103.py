from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import switch_then_move_energy

card = SupporterCardDef(
    guid="e16f5557-d6df-53ff-9a85-094cc313b3fb",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ZinniasTrust.Name",
    display_name="Zinnia's Trust",
    searchable_by=["Zinnia's Trust", "Supporter"],
    subtypes=["Supporter"],
    collector_number=103,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    effect=switch_then_move_energy()
)
