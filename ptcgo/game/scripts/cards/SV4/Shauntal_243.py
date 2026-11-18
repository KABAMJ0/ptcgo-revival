from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_switch_either

card = SupporterCardDef(
    guid="4f5fcdd8-f3c4-52b0-857d-c0f1742d5557",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Shauntal.Name",
    display_name="Shauntal",
    searchable_by=["Shauntal", "Supporter"],
    subtypes=["Supporter"],
    collector_number=243,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=flip_switch_either()
)
