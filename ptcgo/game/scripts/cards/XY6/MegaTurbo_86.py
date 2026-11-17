from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="93d6b5c7-727b-5ba2-9c76-86b3b5e33917",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaTurbo.Name",
    display_name="Mega Turbo",
    searchable_by=["Mega Turbo", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=attach_from_discard(is_basic_energy_card, count=1, target="choice")
)
