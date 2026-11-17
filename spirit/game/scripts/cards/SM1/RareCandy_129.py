from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import evolve_from_hand

card = ItemCardDef(
    guid="5ec593f9-b816-5895-99ac-459c66f0edc5",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=evolve_from_hand()
)
