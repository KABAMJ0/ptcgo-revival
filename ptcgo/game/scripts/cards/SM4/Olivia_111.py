from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_pokemon_gx

card = SupporterCardDef(
    guid="8311aa5c-45d0-58a7-8194-c16ff88f14a6",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Olivia.Name",
    display_name="Olivia",
    searchable_by=["Olivia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="SM4",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(is_pokemon_gx, count=2)
)
