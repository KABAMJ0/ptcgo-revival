from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="21203d92-01e2-5ef5-98a5-e62266cc3807",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsLetter.Name",
    display_name="Professor's Letter",
    searchable_by=["Professor's Letter", "Item"],
    subtypes=["Item"],
    collector_number=123,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
