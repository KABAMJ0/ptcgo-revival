from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import escape_rope

card = ItemCardDef(
    guid="7791ed2e-a676-504a-af84-ceaeee414e35",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EscapeRope.Name",
    display_name="Escape Rope",
    searchable_by=["Escape Rope", "Item"],
    subtypes=["Item"],
    collector_number=127,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=escape_rope
)
