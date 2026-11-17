from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_bench_to_active

card = SupporterCardDef(
    guid="4089116a-d950-5483-b3ea-7f340ebaa36a",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BosssOrdersGhetsis.Name",
    display_name="Boss's Orders (Ghetsis)",
    searchable_by=["Boss's Orders (Ghetsis)", "Supporter"],
    subtypes=["Supporter"],
    collector_number=248,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=opponent_bench_to_active()
)
