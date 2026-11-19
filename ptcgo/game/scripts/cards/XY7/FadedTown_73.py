from ptcgo.game.data_utils import StadiumCardDef, unimplemented, Ability, Triggers
from ptcgo.game.card_effects.support_common import counters_each_in_play
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype
from ptcgo.game.attributes import Rarities

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
        title="FadedTown_73",
        trigger=Triggers.BETWEEN_TURNS,
        effect=counters_each_in_play(2, lambda p: has_pokemon_subtype(p, "MEGA")),
    )
)
