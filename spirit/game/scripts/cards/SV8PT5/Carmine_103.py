from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="2f65b11b-3645-54ae-8d56-05c15272c95e",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Carmine.Name",
    display_name="Carmine",
    searchable_by=["Carmine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=103,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=discard_hand_draw(5)
)
