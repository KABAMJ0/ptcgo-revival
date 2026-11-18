from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.card_effects.trainers import stadium_checkup_counters, pokemon_has_any_subtype

card = StadiumCardDef(
    guid="8a45285d-5497-5c7d-b540-9da6304eaca6",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShrineofPunishment.Name",
    display_name="Shrine of Punishment",
    searchable_by=["Shrine of Punishment", "Stadium"],
    subtypes=["Stadium"],
    collector_number=90,
    set_code="SVault",
    rarity=Rarities.RareSecret,
    ability=Ability(
        title="Shrine of Punishment",
        trigger=Triggers.BETWEEN_TURNS,
        effect=stadium_checkup_counters(1, pokemon_has_any_subtype("GX", "EX")),
    ),
)
