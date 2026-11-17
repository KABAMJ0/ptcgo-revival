from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_pokemon

card = SupporterCardDef(
    guid="2eea6736-f3b1-5c8f-abcc-8ee163897512",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonFanClub.Name",
    display_name="Pokémon Fan Club",
    searchable_by=["Pok\u00e9mon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=155,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(is_basic_pokemon, count=2)
)
