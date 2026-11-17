from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import look_top_reorder

card = ItemCardDef(
    guid="b8ddbc72-9ceb-5ecd-bc47-9869b769a3e1",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokdex.Name",
    display_name="Pokédex",
    searchable_by=["Pok\u00e9dex"],
    subtypes=[],
    collector_number=115,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    effect=look_top_reorder(5)
)
