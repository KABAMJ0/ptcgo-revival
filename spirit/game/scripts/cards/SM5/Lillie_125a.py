from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import first_turn_draw_until

card = SupporterCardDef(
    guid="27d7e715-a52b-5196-83a2-63e4b0a10361",
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
