from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import first_turn_draw_until

card = SupporterCardDef(
    guid="0bdec72a-fa96-5cd7-804e-f2acb9a0a479",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lillie.Name",
    display_name="Lillie",
    searchable_by=["Lillie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=62,
    set_code="SL",
    rarity=Rarities.Uncommon,
    effect=first_turn_draw_until(6, 8)
)
