from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import copycat_draw

card = SupporterCardDef(
    guid="5b4345fc-a8f6-5bf2-bd1e-a865ac7d503b",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name",
    display_name="Copycat",
    searchable_by=["Copycat", "Supporter"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=copycat_draw()
)
