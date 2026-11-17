from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import first_turn_draw_until

card = SupporterCardDef(
    guid="2db7c53e-bd48-513b-9eae-676c71fd3d6f",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lillie.Name",
    display_name="Lillie",
    searchable_by=["Lillie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=125,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=first_turn_draw_until(6, 8)
)
