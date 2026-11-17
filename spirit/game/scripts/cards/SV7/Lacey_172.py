from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_prizes_low, shuffle_hand_draw

card = SupporterCardDef(
    guid="0c51c97b-da26-5ad6-9adf-178285a730ed",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lacey.Name",
    display_name="Lacey",
    searchable_by=["Lacey", "Supporter"],
    subtypes=["Supporter"],
    collector_number=172,
    set_code="SV7",
    rarity=Rarities.Rare,
    effect=shuffle_hand_draw(4, opponent_prizes_low=(3, 8))
)
