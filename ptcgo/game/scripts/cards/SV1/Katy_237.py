from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import ends_turn_after, shuffle_hand_draw

card = SupporterCardDef(
    guid="7b9f6dfa-1f48-5bd8-a18c-8ad942cf30e5",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Katy.Name",
    display_name="Katy",
    searchable_by=["Katy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=237,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=ends_turn_after(shuffle_hand_draw(8))
)
