from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="4c7f6e1c-bd38-5c89-9be8-20fa2fa5035f",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Carmine.Name",
    display_name="Carmine",
    searchable_by=["Carmine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    effect=discard_hand_draw(5)
)
