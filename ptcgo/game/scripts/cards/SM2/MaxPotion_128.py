from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_all_then_discard_energy

card = ItemCardDef(
    guid="b2dcfc2b-bf83-51aa-8674-1b9090ea73f2",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxPotion.Name",
    display_name="Max Potion",
    searchable_by=["Max Potion", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=heal_all_then_discard_energy()
)
