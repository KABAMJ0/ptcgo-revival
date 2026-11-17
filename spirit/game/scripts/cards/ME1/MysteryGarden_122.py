from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_until_per_typed_pokemon, stadium_ability, with_discard_cost

card = StadiumCardDef(
    guid="242afd0a-05d4-5ab4-be56-29ca112022f3",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryGarden.Name",
    display_name="Mystery Garden",
    searchable_by=["Mystery Garden", "Stadium"],
    subtypes=["Stadium"],
    collector_number=122,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Mystery Garden', with_discard_cost(1, draw_until_per_typed_pokemon("psychic")))
)
