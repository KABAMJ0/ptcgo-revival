from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.card_effects.trainers import draw_until_then_turn_ends, stadium_ability
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="96cb9e70-2675-5489-b133-2f3f1d795aa9",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalBeach.Name",
    display_name="Tropical Beach",
    searchable_by=["Tropical Beach", "Stadium"],
    subtypes=["Stadium"],
    collector_number=50,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    ability=stadium_ability('Tropical Beach', draw_until_then_turn_ends(7))
)
