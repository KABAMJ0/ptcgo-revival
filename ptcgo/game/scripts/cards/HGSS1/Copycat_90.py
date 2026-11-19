from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import copycat_draw

card = SupporterCardDef(
    guid="2da4aa41-0645-5edf-8d35-91f7d41380c7",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name",
    display_name="Copycat",
    searchable_by=["Copycat", "Supporter"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=copycat_draw()
)
