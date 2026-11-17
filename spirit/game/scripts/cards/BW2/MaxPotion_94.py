from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import heal_all_then_discard_energy

card = ItemCardDef(
    guid="39f31153-95cb-5e2e-981a-03586849ba61",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxPotion.Name",
    display_name="Max Potion",
    searchable_by=["Max Potion", "Item"],
    subtypes=["Item"],
    collector_number=94,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    effect=heal_all_then_discard_energy()
)
