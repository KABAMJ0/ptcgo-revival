from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_top_discard_rest_back

card = SupporterCardDef(
    guid="6e417334-b803-5531-b7d6-ad13fd298712",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Raifort.Name",
    display_name="Raifort",
    searchable_by=["Raifort", "Supporter"],
    subtypes=["Supporter"],
    collector_number=161,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    effect=look_top_discard_rest_back(5)
)
