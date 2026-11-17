from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_pokemon_card, marnie, owned_by, stadium_ability

card = StadiumCardDef(
    guid="1732c541-809d-518c-8a72-55d96a921581",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpikemuthGym.Name",
    display_name="Spikemuth Gym",
    searchable_by=["Spikemuth Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=169,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Spikemuth Gym', search_to_hand(all_of(is_pokemon_card, owned_by("marnie")), count=1))
)
