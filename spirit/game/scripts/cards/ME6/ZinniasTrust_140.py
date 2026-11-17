from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import switch_then_move_energy

card = SupporterCardDef(
    guid="c5d21e36-1719-5453-b45b-c7fe83d0b789",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ZinniasTrust.Name",
    display_name="Zinnia's Trust",
    searchable_by=["Zinnia's Trust", "Supporter"],
    subtypes=["Supporter"],
    collector_number=140,
    set_code="ME6",
    rarity=Rarities.Rare,
    effect=switch_then_move_energy()
)
