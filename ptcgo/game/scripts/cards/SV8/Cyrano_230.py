from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_pokemon_ex

card = SupporterCardDef(
    guid="dc705ed1-35e5-5b5c-a44c-2e93bd1189d7",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cyrano.Name",
    display_name="Cyrano",
    searchable_by=["Cyrano", "Supporter"],
    subtypes=["Supporter"],
    collector_number=230,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=search_to_hand(is_pokemon_ex, count=3)
)
