from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import _missing_clover

card = ItemCardDef(
    guid="f4f75452-c5dd-52c5-bc11-0c8d9522f3bd",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MissingClover.Name",
    display_name="Missing Clover",
    searchable_by=["Missing Clover", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=_missing_clover,
)
