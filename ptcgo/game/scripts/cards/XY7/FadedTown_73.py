from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.card_effects.trainers import stadium_checkup_counters, pokemon_has_any_subtype

card = StadiumCardDef(
    guid="7c3fbfb4-e8e8-5fba-aa41-921b5747b179",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FadedTown.Name",
    display_name="Faded Town",
    searchable_by=["Faded Town", "Stadium"],
    subtypes=["Stadium"],
    collector_number=73,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Faded Town",
        trigger=Triggers.BETWEEN_TURNS,
        effect=stadium_checkup_counters(2, pokemon_has_any_subtype("MEGA")),
    ),
)
