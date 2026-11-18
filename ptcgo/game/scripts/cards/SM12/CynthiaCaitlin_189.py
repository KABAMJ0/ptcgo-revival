from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import cynthia_caitlin

card = SupporterCardDef(
    guid="e9c83471-65c5-5038-b053-46426391fc43",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiaCaitlin.Name",
    display_name="Cynthia & Caitlin",
    searchable_by=["Cynthia & Caitlin", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=189,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=cynthia_caitlin(3)
)
