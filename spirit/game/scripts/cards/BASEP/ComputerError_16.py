from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ced2852a-9882-5a57-bf3b-105836f051ee",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ComputerError.Name",
    display_name="Computer Error",
    searchable_by=["Computer Error", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=16,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
