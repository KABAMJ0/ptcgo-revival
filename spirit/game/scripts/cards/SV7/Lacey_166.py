from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_prizes_low, shuffle_hand_draw

card = SupporterCardDef(
    guid="ddc253a4-ceed-520a-a47a-02515f001b3f",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lacey.Name",
    display_name="Lacey",
    searchable_by=["Lacey", "Supporter"],
    subtypes=["Supporter"],
    collector_number=166,
    set_code="SV7",
    rarity=Rarities.Rare,
    effect=shuffle_hand_draw(4, opponent_prizes_low=(3, 8))
)
