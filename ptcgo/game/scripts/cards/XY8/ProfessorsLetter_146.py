from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="b4a1df6a-1d88-5214-952e-8860e356517b",
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
