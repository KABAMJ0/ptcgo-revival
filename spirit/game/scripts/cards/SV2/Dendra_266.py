from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_to_bottom_draw_until

card = SupporterCardDef(
    guid="876de441-fb09-5114-bf1a-eb0595c299a6",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dendra.Name",
    display_name="Dendra",
    searchable_by=["Dendra", "Supporter"],
    subtypes=["Supporter"],
    collector_number=266,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=hand_to_bottom_draw_until(5)
)
