from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import copycat_draw

card = SupporterCardDef(
    guid="74417b45-d822-539c-8b8c-93b33002eb85",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name",
    display_name="Copycat",
    searchable_by=["Copycat", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    effect=copycat_draw()
)
