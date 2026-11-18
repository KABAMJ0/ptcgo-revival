from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_all_then_discard_energy

card = ItemCardDef(
    guid="1f4063bc-ee32-5b49-ac6e-fdba8fd60247",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxPotion.Name",
    display_name="Max Potion",
    searchable_by=["Max Potion", "Item"],
    subtypes=["Item"],
    collector_number=164,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    effect=heal_all_then_discard_energy()
)
