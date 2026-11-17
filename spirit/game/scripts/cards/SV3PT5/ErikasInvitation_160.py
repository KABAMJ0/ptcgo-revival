from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_bench_from_hand_then_switch

card = SupporterCardDef(
    guid="1fdd21cb-42ef-50ac-8c2c-4cbb34b65f55",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasInvitation.Name",
    display_name="Erika's Invitation",
    searchable_by=["Erika's Invitation", "Supporter"],
    subtypes=["Supporter"],
    collector_number=160,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_from_hand_then_switch()
)
