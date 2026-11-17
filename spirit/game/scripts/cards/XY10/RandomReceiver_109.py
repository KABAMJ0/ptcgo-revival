from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import reveal_until_supporter

card = ItemCardDef(
    guid="86e2527a-3144-5882-8aeb-902e28be98c8",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RandomReceiver.Name",
    display_name="Random Receiver",
    searchable_by=["Random Receiver", "Item"],
    subtypes=["Item"],
    collector_number=109,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=reveal_until_supporter()
)
