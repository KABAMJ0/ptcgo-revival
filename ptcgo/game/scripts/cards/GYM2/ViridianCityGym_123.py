from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.card_effects.trainers import stadium_evolve_heal

card = StadiumCardDef(
    guid="ebf437b8-1aed-58a3-a919-6dcf794937d8",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ViridianCityGym.Name",
    display_name="Viridian City Gym",
    searchable_by=["Viridian City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=123,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Viridian City Gym",
        trigger=Triggers.ON_EVOLVE,
        effect=stadium_evolve_heal(2, "Giovanni", only_one_left=1),
    ),
)
