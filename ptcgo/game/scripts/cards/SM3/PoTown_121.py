from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.card_effects.trainers import stadium_evolve_counters

card = StadiumCardDef(
    guid="47e7adfc-ca5b-5eaf-ab1e-cf478e51515d",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PoTown.Name",
    display_name="Po Town",
    searchable_by=["Po Town", "Stadium"],
    subtypes=["Stadium"],
    collector_number=121,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Po Town",
        trigger=Triggers.ON_EVOLVE,
        effect=stadium_evolve_counters(3),
    ),
)
