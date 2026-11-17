from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import basic_energy_of

card = ItemCardDef(
    guid="9fb81d10-cb62-52ca-97f8-af0e1ad772fe",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AquaPatch.Name",
    display_name="Aqua Patch",
    searchable_by=["Aqua Patch", "Item"],
    subtypes=["Item"],
    collector_number=161,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    effect=attach_from_discard(basic_energy_of("water"), count=1, target="choice")
)
