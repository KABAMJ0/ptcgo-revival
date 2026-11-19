from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import resistance_reduced_passive

card = StadiumCardDef(
    guid="3414be12-a0f0-59ad-9cdd-a7ec9a2d91b6",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ResistanceGym.Name",
    display_name="Resistance Gym",
    searchable_by=["Resistance Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=109,
    set_code="GYM2",
    rarity=Rarities.Rare,
    passive=resistance_reduced_passive(20)
)
