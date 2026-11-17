from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_to_bottom_draw_until

card = SupporterCardDef(
    guid="2c261fea-06ce-563e-8950-0418aea7fd00",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dendra.Name",
    display_name="Dendra",
    searchable_by=["Dendra", "Supporter"],
    subtypes=["Supporter"],
    collector_number=250,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=hand_to_bottom_draw_until(5)
)
