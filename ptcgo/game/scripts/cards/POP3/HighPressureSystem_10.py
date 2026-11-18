from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_retreat_discount_typed

card = StadiumCardDef(
    guid="22d23a20-bb72-53d7-8e09-a339d007e94c",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HighPressureSystem.Name",
    display_name="High Pressure System",
    searchable_by=["High Pressure System", "Stadium"],
    subtypes=["Stadium"],
    collector_number=10,
    set_code="POP3",
    rarity=Rarities.Uncommon,
    passive=stadium_retreat_discount_typed("fire", "water")
)
