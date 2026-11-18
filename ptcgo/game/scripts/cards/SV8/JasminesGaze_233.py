from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import jasmine_gaze

card = SupporterCardDef(
    guid="b44746f5-73f6-5e78-819e-b4476f33eb62",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JasminesGaze.Name",
    display_name="Jasmine's Gaze",
    searchable_by=["Jasmine's Gaze", "Supporter"],
    subtypes=["Supporter"],
    collector_number=233,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=jasmine_gaze()
)
