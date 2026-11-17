from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_bench_from_hand_then_switch

card = SupporterCardDef(
    guid="c4bc9e2a-fa19-5651-9734-fcde755219b4",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasInvitation.Name",
    display_name="Erika's Invitation",
    searchable_by=["Erika's Invitation", "Supporter"],
    subtypes=["Supporter"],
    collector_number=196,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    effect=opponent_bench_from_hand_then_switch()
)
