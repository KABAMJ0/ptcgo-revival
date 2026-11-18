from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.card_effects.trainers import stadium_checkup_counters, pokemon_has_any_subtype

card = StadiumCardDef(
    guid="f3eb7eaf-99b4-5356-9f22-2039c546c38f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShrineofPunishment.Name",
    display_name="Shrine of Punishment",
    searchable_by=["Shrine of Punishment", "Stadium"],
    subtypes=["Stadium"],
    collector_number=143,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Shrine of Punishment",
        trigger=Triggers.BETWEEN_TURNS,
        effect=stadium_checkup_counters(1, pokemon_has_any_subtype("GX", "EX")),
    ),
)
