from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import all_of, is_basic_energy_card, is_pokemon_card

card = SupporterCardDef(
    guid="9a9ff7e9-7328-5ce7-b42d-a99100c931d3",
    key="SM115",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name",
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=53,
    set_code="SM115",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(all_of(is_pokemon_card, is_basic_energy_card), count=6, to="deck_shuffle")
)
