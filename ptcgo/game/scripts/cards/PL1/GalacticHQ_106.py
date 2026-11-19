from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.card_effects.trainers import stadium_evolve_counters

card = StadiumCardDef(
    guid="6bced9bf-c2a0-53ff-8dc7-0830434aab9e",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GalacticHQ.Name",
    display_name="Galactic HQ",
    searchable_by=["Galactic HQ", "Stadium"],
    subtypes=["Stadium"],
    collector_number=106,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Galactic HQ",
        trigger=Triggers.ON_EVOLVE,
        effect=stadium_evolve_counters(2),
    ),
)
