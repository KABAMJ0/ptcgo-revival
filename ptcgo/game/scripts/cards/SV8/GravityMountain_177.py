from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_stage_two, stadium_hp_bonus

card = StadiumCardDef(
    guid="92e8c82b-66cd-592d-b931-1174c4e32ff8",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GravityMountain.Name",
    display_name="Gravity Mountain",
    searchable_by=["Gravity Mountain", "Stadium"],
    subtypes=["Stadium"],
    collector_number=177,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    passive=stadium_hp_bonus(30, is_stage_two)
)
