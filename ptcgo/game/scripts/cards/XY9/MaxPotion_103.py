from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_all_then_discard_energy

card = ItemCardDef(
    guid="baf7d106-d4f8-5fa8-b328-dbe3a444c0ee",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxPotion.Name",
    display_name="Max Potion",
    searchable_by=["Max Potion", "Item"],
    subtypes=["Item"],
    collector_number=103,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=heal_all_then_discard_energy(),
)
