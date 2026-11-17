from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c32d115b-99f9-5088-b666-b13c677efff8",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CardFlipGame.Name",
    display_name="Card-Flip Game",
    searchable_by=["Card-Flip Game", "Goldenrod Game Corner"],
    subtypes=["Goldenrod Game Corner"],
    collector_number=92,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
