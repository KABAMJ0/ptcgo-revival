from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_until_per_typed_pokemon, stadium_ability, with_discard_cost

card = StadiumCardDef(
    guid="12beb776-fac9-5a2d-939e-22666eab1187",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryGarden.Name",
    display_name="Mystery Garden",
    searchable_by=["Mystery Garden", "Stadium"],
    subtypes=["Stadium"],
    collector_number=172,
    set_code="ME1",
    rarity=Rarities.Rare,
    ability=stadium_ability('Mystery Garden', with_discard_cost(1, draw_until_per_typed_pokemon("psychic")))
)
