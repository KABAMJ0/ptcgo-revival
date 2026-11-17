from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_prizes_low, shuffle_hand_draw

card = SupporterCardDef(
    guid="6b301027-76de-5f79-8d82-d7db4b3aafc9",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lacey.Name",
    display_name="Lacey",
    searchable_by=["Lacey", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=shuffle_hand_draw(4, opponent_prizes_low=(3, 8))
)
