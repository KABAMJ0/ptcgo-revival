from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_rule_box_free_plus_students

card = SupporterCardDef(
    guid="1228d521-b8c9-53f2-a20e-64157577550c",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PaldeanStudent.Name",
    display_name="Paldean Student",
    searchable_by=["Paldean Student", "Supporter"],
    subtypes=["Supporter"],
    collector_number=230,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    effect=search_rule_box_free_plus_students("paldean student")
)
