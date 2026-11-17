from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import basic_energy_of, stadium_ability, with_discard_cost

card = StadiumCardDef(
    guid="224166b3-5efc-5add-93c4-e4e4473e6622",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiantHearth.Name",
    display_name="Giant Hearth",
    searchable_by=["Giant Hearth", "Stadium"],
    subtypes=["Stadium"],
    collector_number=263,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    ability=stadium_ability('Giant Hearth', with_discard_cost(1, search_to_hand(basic_energy_of("fire"), count=2)))
)
