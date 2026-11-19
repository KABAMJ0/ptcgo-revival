from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import heal_multiplier

card = StadiumCardDef(
    guid="19c7951a-75b0-5cd9-8ee2-d8c82074bec8",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LegendaryTrench.Name",
    display_name="Legendary Trench",
    searchable_by=["Legendary Trench", "Stadium"],
    subtypes=["Stadium"],
    collector_number=99,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    passive=heal_multiplier(multiply=2)
)
