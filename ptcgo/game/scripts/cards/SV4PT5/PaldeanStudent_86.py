from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_rule_box_free_plus_students

card = SupporterCardDef(
    guid="20cbf1fa-c75b-5fac-afad-fe3bb0cc586c",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PaldeanStudent.Name",
    display_name="Paldean Student",
    searchable_by=["Paldean Student", "Supporter"],
    subtypes=["Supporter"],
    collector_number=86,
    set_code="SV4PT5",
    rarity=Rarities.Common,
    effect=search_rule_box_free_plus_students("paldean student")
)
