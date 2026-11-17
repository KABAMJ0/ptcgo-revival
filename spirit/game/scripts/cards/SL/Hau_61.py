from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="f986bbdd-f51b-59df-9514-aab3c7e7888f",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hau.Name",
    display_name="Hau",
    searchable_by=["Hau", "Supporter"],
    subtypes=["Supporter"],
    collector_number=61,
    set_code="SL",
    rarity=Rarities.Uncommon,
    effect=draw_n(3)
)
