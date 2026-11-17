from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import any_of, is_basic_energy_card, is_pokemon_card

card = SupporterCardDef(
    guid="e703f9a4-c65c-5aa4-9bb3-882776f76a87",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PalmersContribution.Name",
    display_name="Palmer's Contribution",
    searchable_by=["Palmer's Contribution", "Supporter"],
    subtypes=["Supporter"],
    collector_number=139,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(any_of(is_pokemon_card, is_basic_energy_card), count=5, to="deck_shuffle")
)
