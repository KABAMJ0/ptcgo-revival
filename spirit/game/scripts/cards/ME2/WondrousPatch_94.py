from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import basic_energy_of

card = ItemCardDef(
    guid="6f13739e-b910-5ab1-841c-ddde84ebb3cd",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WondrousPatch.Name",
    display_name="Wondrous Patch",
    searchable_by=["Wondrous Patch", "Item"],
    subtypes=["Item"],
    collector_number=94,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    effect=attach_from_discard(basic_energy_of("psychic"), count=1, target="choice")
)
