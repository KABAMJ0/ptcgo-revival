from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import ends_turn_after, shuffle_hand_draw

card = SupporterCardDef(
    guid="97c80094-c35b-5cf7-a0ba-b8bcf0e9d1be",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Katy.Name",
    display_name="Katy",
    searchable_by=["Katy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=ends_turn_after(shuffle_hand_draw(8))
)
