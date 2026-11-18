from ptcgo.game.card_effects.trainers import PRIMORDIAL_ALTAR_ABILITY
from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="8cbeeee2-0e1d-5a41-9851-cb2e090c6820",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PrimordialAltar.Name",
    display_name="Primordial Altar",
    searchable_by=["Primordial Altar", "Stadium"],
    subtypes=["Stadium"],
    collector_number=161,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    ability=PRIMORDIAL_ALTAR_ABILITY,
)
