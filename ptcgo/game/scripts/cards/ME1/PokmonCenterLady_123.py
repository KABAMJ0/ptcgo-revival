from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = SupporterCardDef(
    guid="2b2ad67f-dcd6-5048-9754-15c0c436d6e1",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCenterLady.Name",
    display_name="Pokémon Center Lady",
    searchable_by=["Pok\u00e9mon Center Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="ME1",
    rarity=Rarities.Common,
    effect=heal_item(amount=60, scope="choice", condition_cure=True)
)
