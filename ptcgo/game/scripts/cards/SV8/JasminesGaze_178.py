from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import jasmine_gaze

card = SupporterCardDef(
    guid="1ff40e39-6d3a-5316-83ff-814875b5e872",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JasminesGaze.Name",
    display_name="Jasmine's Gaze",
    searchable_by=["Jasmine's Gaze", "Supporter"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=jasmine_gaze()
)
