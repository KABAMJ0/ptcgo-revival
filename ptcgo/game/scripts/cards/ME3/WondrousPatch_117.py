from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of

card = ItemCardDef(
    guid="c6657dc3-d9f6-5481-a3c5-86a429805ee1",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WondrousPatch.Name",
    display_name="Wondrous Patch",
    searchable_by=["Wondrous Patch", "Item"],
    subtypes=["Item"],
    collector_number=117,
    set_code="ME3",
    rarity=Rarities.Rare,
    effect=attach_from_discard(basic_energy_of("psychic"), count=1, target="choice")
)
