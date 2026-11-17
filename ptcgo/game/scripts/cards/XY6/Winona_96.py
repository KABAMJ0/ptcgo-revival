from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import pokemon_of

card = SupporterCardDef(
    guid="2d508c1f-20bd-592d-a839-2043f63b4385",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Winona.Name",
    display_name="Winona",
    searchable_by=["Winona", "Supporter"],
    subtypes=["Supporter"],
    collector_number=96,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(pokemon_of("colorless"), count=3)
)
