from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_top_pick_one_back

card = ItemCardDef(
    guid="06f9d510-ef03-5437-b9bd-5f1e0cfa3d77",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChipChipIceAxe.Name",
    display_name="Chip-Chip Ice Axe",
    searchable_by=["Chip-Chip Ice Axe", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=look_top_pick_one_back(3, owner="opponent")
)
