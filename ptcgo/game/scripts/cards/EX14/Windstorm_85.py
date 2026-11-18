from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_tools_and_stadium

card = ItemCardDef(
    guid="db3d3b1c-9b4b-5089-989b-7f0711b2423d",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Windstorm.Name",
    display_name="Windstorm",
    searchable_by=["Windstorm", "Item"],
    subtypes=["Item"],
    collector_number=85,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=discard_tools_and_stadium(2)
)
