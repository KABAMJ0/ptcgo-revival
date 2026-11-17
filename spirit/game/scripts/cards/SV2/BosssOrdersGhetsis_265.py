from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_bench_to_active

card = SupporterCardDef(
    guid="d835251a-14b3-5212-b398-20de5174b3dc",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BosssOrdersGhetsis.Name",
    display_name="Boss's Orders (Ghetsis)",
    searchable_by=["Boss's Orders (Ghetsis)", "Supporter"],
    subtypes=["Supporter"],
    collector_number=265,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=opponent_bench_to_active()
)
