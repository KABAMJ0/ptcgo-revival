from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_from_bottom

card = SupporterCardDef(
    guid="3e2c8e76-01f3-5f57-85d1-57f5c67d0def",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Looker.Name",
    display_name="Looker",
    searchable_by=["Looker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=126,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=draw_from_bottom(3)
)
