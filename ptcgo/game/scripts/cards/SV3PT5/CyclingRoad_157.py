from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_typed_from_hand_then, is_basic_energy_card, stadium_ability

card = StadiumCardDef(
    guid="adbcba36-4bf2-519f-a3cc-23f3f588dbc5",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CyclingRoad.Name",
    display_name="Cycling Road",
    searchable_by=["Cycling Road", "Stadium"],
    subtypes=["Stadium"],
    collector_number=157,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Cycling Road', discard_typed_from_hand_then(is_basic_energy_card, 1, lambda ctx: ctx.draw_cards(1)))
)
