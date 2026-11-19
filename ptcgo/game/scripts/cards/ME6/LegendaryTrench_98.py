from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import heal_multiplier

card = StadiumCardDef(
    guid="85edb2c2-f7d6-5e7d-86bc-5e94f14f99be",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LegendaryTrench.Name",
    display_name="Legendary Trench",
    searchable_by=["Legendary Trench", "Stadium"],
    subtypes=["Stadium"],
    collector_number=98,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    passive=heal_multiplier(multiply=2)
)
