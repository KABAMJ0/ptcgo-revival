from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.card_effects.trainers import draw_until_then_turn_ends, stadium_ability
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="00e32750-f213-5b23-b831-32571ec1aaa1",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalBeach.Name",
    display_name="Tropical Beach",
    searchable_by=["Tropical Beach", "Stadium"],
    subtypes=["Stadium"],
    collector_number=28,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    ability=stadium_ability('Tropical Beach', draw_until_then_turn_ends(7))
)
