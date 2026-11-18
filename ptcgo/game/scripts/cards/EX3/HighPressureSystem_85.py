from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_retreat_discount_typed

card = StadiumCardDef(
    guid="09d88e23-ac14-5d36-8758-156b04401644",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HighPressureSystem.Name",
    display_name="High Pressure System",
    searchable_by=["High Pressure System", "Stadium"],
    subtypes=["Stadium"],
    collector_number=85,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    passive=stadium_retreat_discount_typed("fire", "water")
)
