from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_switch_either

card = SupporterCardDef(
    guid="9a6fd652-cd10-5b24-93f0-6b475dbde8c7",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Shauntal.Name",
    display_name="Shauntal",
    searchable_by=["Shauntal", "Supporter"],
    subtypes=["Supporter"],
    collector_number=174,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    effect=flip_switch_either()
)
