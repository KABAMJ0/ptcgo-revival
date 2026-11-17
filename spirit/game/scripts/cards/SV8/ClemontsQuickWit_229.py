from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import heal_each_typed

card = SupporterCardDef(
    guid="068e17e3-36f2-56c4-91e1-d2273b9cdefe",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClemontsQuickWit.Name",
    display_name="Clemont's Quick Wit",
    searchable_by=["Clemont's Quick Wit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=229,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=heal_each_typed(60, "lightning")
)
