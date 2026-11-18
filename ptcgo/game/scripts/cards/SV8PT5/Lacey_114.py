from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_prizes_low, shuffle_hand_draw

card = SupporterCardDef(
    guid="0ac20f5f-51c7-505c-82b8-2833b1b10bc3",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lacey.Name",
    display_name="Lacey",
    searchable_by=["Lacey", "Supporter"],
    subtypes=["Supporter"],
    collector_number=114,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw(4, opponent_prizes_low=(3, 8))
)
