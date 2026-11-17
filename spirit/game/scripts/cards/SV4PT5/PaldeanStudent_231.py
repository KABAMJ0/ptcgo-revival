from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import search_rule_box_free_plus_students

card = SupporterCardDef(
    guid="41bb20a8-757e-505c-82a5-30d30b7e7344",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PaldeanStudent.Name",
    display_name="Paldean Student",
    searchable_by=["Paldean Student", "Supporter"],
    subtypes=["Supporter"],
    collector_number=231,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    effect=search_rule_box_free_plus_students("paldean student")
)
