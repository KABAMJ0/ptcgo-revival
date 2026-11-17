from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import all_of, is_basic_energy_card, is_pokemon_card

card = SupporterCardDef(
    guid="9754b007-d18c-5bb8-9841-225b9bfccc4f",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name",
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=135,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(all_of(is_pokemon_card, is_basic_energy_card), count=6, to="deck_shuffle")
)
