from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="22a1bc19-f276-5167-bc71-9b1e4bf2c3f3",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Carmine.Name",
    display_name="Carmine",
    searchable_by=["Carmine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=217,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=discard_hand_draw(5)
)
