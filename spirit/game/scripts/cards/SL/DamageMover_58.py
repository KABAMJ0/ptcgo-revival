from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="dc28221b-6481-5d1c-b2a9-209682844fad",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DamageMover.Name",
    display_name="Damage Mover",
    searchable_by=["Damage Mover", "Item"],
    subtypes=["Item"],
    collector_number=58,
    set_code="SL",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
