from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shadow_triad

card = SupporterCardDef(
    guid="459ba560-5f1b-5e37-8d5f-10648eb33d5d",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShadowTriad.Name",
    display_name="Shadow Triad",
    searchable_by=["Shadow Triad", "Supporter", "Team Plasma"],
    subtypes=["Supporter", "Team Plasma"],
    collector_number=102,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    effect=shadow_triad()
)
