from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_top_discard_rest_back

card = SupporterCardDef(
    guid="412c9f61-63f0-5d82-a69f-a612319a665e",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Raifort.Name",
    display_name="Raifort",
    searchable_by=["Raifort", "Supporter"],
    subtypes=["Supporter"],
    collector_number=142,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=look_top_discard_rest_back(5)
)
