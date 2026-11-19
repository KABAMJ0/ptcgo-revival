from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import choose_one, is_basic_energy_card
from ptcgo.game.card_effects.support_common import recover_from_discard, search_to_hand

_MR_STONES_PROJECT = choose_one([
    ("Search your deck", search_to_hand(is_basic_energy_card, 2)),
    ("Search your discard pile",
     recover_from_discard(is_basic_energy_card, 2, minimum=0, reveal=True)),
])


card = SupporterCardDef(
    guid="405bfbf7-8529-50a7-a5c2-aa09a0d86950",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MrStonesProject.Name",
    display_name="Mr. Stone's Project",
    searchable_by=["Mr. Stone's Project", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    effect=_MR_STONES_PROJECT
)
