from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="38c48494-617e-54a5-81b8-b4c0e3cdcf77",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsLetter.Name",
    display_name="Professor's Letter",
    searchable_by=["Professor's Letter", "Item"],
    subtypes=["Item"],
    collector_number=146,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_basic_energy_card, count=2)
)
