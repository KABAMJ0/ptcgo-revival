from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_to_top

card = SupporterCardDef(
    guid="61fa91e6-0aa3-5062-be2b-5270a8d21b24",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CiphermaniacsCodebreaking.Name",
    display_name="Ciphermaniac's Codebreaking",
    searchable_by=["Ciphermaniac's Codebreaking", "Supporter", "Future"],
    subtypes=["Supporter", "Future"],
    collector_number=145,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    effect=search_to_top(2)
)
