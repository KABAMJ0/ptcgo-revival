from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_stage_two, stadium_hp_bonus

card = StadiumCardDef(
    guid="f301bab0-74a8-5bf2-b590-d904c4fd20b2",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GravityMountain.Name",
    display_name="Gravity Mountain",
    searchable_by=["Gravity Mountain", "Stadium"],
    subtypes=["Stadium"],
    collector_number=250,
    set_code="SV8",
    rarity=Rarities.Rare,
    passive=stadium_hp_bonus(30, is_stage_two)
)
