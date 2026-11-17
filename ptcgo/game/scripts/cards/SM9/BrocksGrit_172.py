from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import all_of, is_basic_energy_card, is_pokemon_card

card = SupporterCardDef(
    guid="76a5e6ca-7405-5fcb-9e4d-29d4da35c255",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name",
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=172,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=recover_from_discard(all_of(is_pokemon_card, is_basic_energy_card), count=6, to="deck_shuffle")
)
