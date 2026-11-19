from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import opponent_switches


_REPEL = opponent_switches


card = ItemCardDef(
    guid="20cb2f33-aecf-515c-9814-de3290e3e5d0",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Repel.Name",
    display_name="Repel",
    searchable_by=["Repel", "Item"],
    subtypes=["Item"],
    collector_number=126,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    effect=_REPEL
)
