from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = SupporterCardDef(
    guid="6e0a8958-8017-596d-81de-c7752cf814c8",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCenterLady.Name",
    display_name="Pokémon Center Lady",
    searchable_by=["Pok\u00e9mon Center Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=68,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=heal_item(amount=60, scope="choice", condition_cure=True)
)
