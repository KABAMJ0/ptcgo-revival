from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_pokemon

card = SupporterCardDef(
    guid="ff12d892-5b1d-5aca-a2a3-2a0039a4c3fc",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonFanClub.Name",
    display_name="Pokémon Fan Club",
    searchable_by=["Pok\u00e9mon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_basic_pokemon, count=2)
)
