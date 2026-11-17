from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_pokemon_ex

card = SupporterCardDef(
    guid="6dac3731-b1e4-5c98-bc9f-33229a0c158e",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cyrano.Name",
    display_name="Cyrano",
    searchable_by=["Cyrano", "Supporter"],
    subtypes=["Supporter"],
    collector_number=170,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_pokemon_ex, count=3)
)
