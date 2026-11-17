from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card, stadium_ability, with_discard_cost

card = StadiumCardDef(
    guid="097a3578-7537-511d-b4ac-5993524d7b23",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ViridianForest.Name",
    display_name="Viridian Forest",
    searchable_by=["Viridian Forest", "Stadium"],
    subtypes=["Stadium"],
    collector_number=256,
    set_code="SM11",
    rarity=Rarities.RareSecret,
    ability=stadium_ability('Viridian Forest', with_discard_cost(1, search_to_hand(is_basic_energy_card, count=1)))
)
