from ptcgo.game.card_effects.trainers import opponent_prizes_low, roxanne
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="6162f1be-b610-584c-a796-493c16c5bbd9",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Roxanne.Name",
    display_name="Roxanne",
    searchable_by=["Roxanne", "Supporter"],
    subtypes=["Supporter"],
    collector_number=66,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareUltra,
    effect=roxanne,
    condition=opponent_prizes_low,
)
