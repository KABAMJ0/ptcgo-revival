from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import first_turn_draw_until

card = SupporterCardDef(
    guid="f3dd6105-4f4e-5cb9-bd8e-4b93ef6300b8",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lillie.Name",
    display_name="Lillie",
    searchable_by=["Lillie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=122,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=first_turn_draw_until(6, 8)
)
