from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of

card = ItemCardDef(
    guid="c44bc391-e593-5306-890a-219ff24b55e3",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarkPatch.Name",
    display_name="Dark Patch",
    searchable_by=["Dark Patch", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=attach_from_discard(basic_energy_of("darkness"), count=1, target="choice")
)
