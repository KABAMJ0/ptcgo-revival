from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import turn_damage_boost_per_prize

card = SupporterCardDef(
    guid="ea50251c-acc9-52a9-b08a-ed69e761b704",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iris.Name",
    display_name="Iris",
    searchable_by=["Iris", "Supporter"],
    subtypes=["Supporter"],
    collector_number=101,
    set_code="BW10",
    rarity=Rarities.RareUltra,
    effect=turn_damage_boost_per_prize(10)
)
