from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_pokemon

card = SupporterCardDef(
    guid="15785734-44ba-5d54-aeb8-a9cf18304c5a",
    key="G1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonFanClub.Name",
    display_name="Pokémon Fan Club",
    searchable_by=["Pok\u00e9mon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="G1",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_basic_pokemon, count=2)
)
