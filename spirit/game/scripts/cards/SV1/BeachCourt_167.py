from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import stadium_retreat_discount

card = StadiumCardDef(
    guid="4de1e30b-73fc-5ed3-815d-69d6aa6ac57f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeachCourt.Name",
    display_name="Beach Court",
    searchable_by=["Beach Court", "Stadium"],
    subtypes=["Stadium"],
    collector_number=167,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    passive=stadium_retreat_discount(1, basic_only=True)
)
