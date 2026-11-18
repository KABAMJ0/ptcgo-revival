from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, is_stage_one, is_stage_two, stadium_hp_bonus

card = StadiumCardDef(
    guid="9f716805-d6d8-5400-bd3a-d295e751aacd",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrainingCenter.Name",
    display_name="Training Center",
    searchable_by=["Training Center", "Stadium"],
    subtypes=["Stadium"],
    collector_number=102,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    passive=stadium_hp_bonus(30, any_of(is_stage_one, is_stage_two))
)
