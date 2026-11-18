from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_chosen

card = SupporterCardDef(
    guid="1d1c0eef-973a-5e37-a10f-d984b70e7346",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Saguaro.Name",
    display_name="Saguaro",
    searchable_by=["Saguaro", "Supporter"],
    subtypes=["Supporter"],
    collector_number=255,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=heal_chosen(50, count=2)
)
