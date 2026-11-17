from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import all_of, is_basic_energy_card, is_pokemon_card

card = SupporterCardDef(
    guid="84280e62-8e67-5282-b954-38cc270be2f4",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name",
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=74,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(all_of(is_pokemon_card, is_basic_energy_card), count=6, to="deck_shuffle")
)
