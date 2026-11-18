from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, is_item_card, pokemon_of

card = SupporterCardDef(
    guid="50075202-c637-561a-8e05-fa7a17ddf93f",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Korrina.Name",
    display_name="Korrina",
    searchable_by=["Korrina", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(pokemon_of("fighting"), is_item_card), count=1)
)
