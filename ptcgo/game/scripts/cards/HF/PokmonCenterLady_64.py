from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = SupporterCardDef(
    guid="c814e210-ce04-5c6d-9099-12f80c5a0112",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCenterLady.Name",
    display_name="Pokémon Center Lady",
    searchable_by=["Pok\u00e9mon Center Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=64,
    set_code="HF",
    rarity=Rarities.Uncommon,
    effect=heal_item(amount=60, scope="choice", condition_cure=True)
)
