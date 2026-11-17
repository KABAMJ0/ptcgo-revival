from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import basic_energy_of, stadium_ability, with_discard_cost

card = StadiumCardDef(
    guid="dc4ddfa1-db4b-5d2d-859f-bf1af01f7e9d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiantHearth.Name",
    display_name="Giant Hearth",
    searchable_by=["Giant Hearth", "Stadium"],
    subtypes=["Stadium"],
    collector_number=197,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Giant Hearth', with_discard_cost(1, search_to_hand(basic_energy_of("fire"), count=2)))
)
