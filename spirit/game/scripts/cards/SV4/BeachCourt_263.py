from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import stadium_retreat_discount

card = StadiumCardDef(
    guid="e0f4ae71-4871-58be-94ac-a8111152dd7a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeachCourt.Name",
    display_name="Beach Court",
    searchable_by=["Beach Court", "Stadium"],
    subtypes=["Stadium"],
    collector_number=263,
    set_code="SV4",
    rarity=Rarities.Rare,
    passive=stadium_retreat_discount(1, basic_only=True)
)
