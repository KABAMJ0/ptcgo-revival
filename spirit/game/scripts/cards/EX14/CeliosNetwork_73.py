from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, any_of, excluding, is_basic_pokemon, is_evolution_pokemon, is_pokemon_ex

card = SupporterCardDef(
    guid="5277953c-a018-5165-9db2-80ef198b7421",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeliosNetwork.Name",
    display_name="Celio's Network",
    searchable_by=["Celio's Network", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(any_of(is_basic_pokemon, is_evolution_pokemon), excluding(is_pokemon_ex)), count=1)
)
