from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import is_basic_pokemon

card = SupporterCardDef(
    guid="dc213941-179c-5ab2-92d1-a6fd6dac20b4",
    key="POP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonFanClub.Name",
    display_name="Pokémon Fan Club",
    searchable_by=["Pok\u00e9mon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=9,
    set_code="POP4",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(is_basic_pokemon, 2)
)
