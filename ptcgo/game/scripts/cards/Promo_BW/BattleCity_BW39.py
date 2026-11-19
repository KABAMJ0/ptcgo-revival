from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.card_effects.trainers import draw_n, if_heads, stadium_ability
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="c65bccdc-7c69-57a3-8d15-3faf6864b562",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleCity.Name",
    display_name="Battle City",
    searchable_by=["Battle City", "Stadium"],
    subtypes=["Stadium"],
    collector_number=39,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    ability=stadium_ability('Battle City', if_heads(draw_n(1)))
)
