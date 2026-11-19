from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import sleep_recovery_coins

card = StadiumCardDef(
    guid="6bcf5df3-745f-5e2a-be09-5c2424b23593",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SlumberingForest.Name",
    display_name="Slumbering Forest",
    searchable_by=["Slumbering Forest", "Stadium"],
    subtypes=["Stadium"],
    collector_number=207,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    passive=sleep_recovery_coins(2)
)
