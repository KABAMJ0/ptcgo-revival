from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_pokemon

card = SupporterCardDef(
    guid="8ee06ff9-0c5b-51ec-b577-5007520381dd",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCollector.Name",
    display_name="Pokémon Collector",
    searchable_by=["Pok\u00e9mon Collector", "Supporter"],
    subtypes=["Supporter"],
    collector_number=97,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_basic_pokemon, count=3)
)
