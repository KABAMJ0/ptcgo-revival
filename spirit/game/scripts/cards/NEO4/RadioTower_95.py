from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import look_top_peek, stadium_ability

card = StadiumCardDef(
    guid="895f22af-3f5c-50da-96c1-2dcf5ad8327e",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RadioTower.Name",
    display_name="Radio Tower",
    searchable_by=["Radio Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=95,
    set_code="NEO4",
    rarity=Rarities.Rare,
    ability=stadium_ability('Radio Tower', look_top_peek(2))
)
