from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card, stadium_ability, with_discard_cost

card = StadiumCardDef(
    guid="703e2173-f13f-50ed-9daf-9878cfb83ddc",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ViridianForest.Name",
    display_name="Viridian Forest",
    searchable_by=["Viridian Forest", "Stadium"],
    subtypes=["Stadium"],
    collector_number=156,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Viridian Forest', with_discard_cost(1, search_to_hand(is_basic_energy_card, count=1)))
)
