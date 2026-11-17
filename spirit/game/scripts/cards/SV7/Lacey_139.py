from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_prizes_low, shuffle_hand_draw

card = SupporterCardDef(
    guid="1d073d90-7fc1-5f41-82a4-7a809a57eb43",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lacey.Name",
    display_name="Lacey",
    searchable_by=["Lacey", "Supporter"],
    subtypes=["Supporter"],
    collector_number=139,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw(4, opponent_prizes_low=(3, 8))
)
