from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_stage_one, stadium_damage_boost

card = StadiumCardDef(
    guid="9a22b83b-1602-5a98-9ecd-6d55c80164dd",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PracticeStudio.Name",
    display_name="Practice Studio",
    searchable_by=["Practice Studio", "Stadium"],
    subtypes=["Stadium"],
    collector_number=186,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    passive=stadium_damage_boost(10, is_stage_one, target=None)
)
