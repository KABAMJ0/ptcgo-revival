from ptcgo.game.card_effects.trainers import copycat_draw
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import copycat_draw


card = SupporterCardDef(
    guid="7ba71e38-118d-5a54-b9f5-7c81dff6dcc5",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name",
    display_name="Copycat",
    searchable_by=["Copycat", "Supporter"],
    subtypes=["Supporter"],
    collector_number=127,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=copycat_draw()
)
