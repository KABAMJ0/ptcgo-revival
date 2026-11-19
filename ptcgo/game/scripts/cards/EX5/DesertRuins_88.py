from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.card_effects.trainers import stadium_checkup_counters, pokemon_is_ex_with_hp

card = StadiumCardDef(
    guid="e17f316c-a8b4-558f-ac0e-b86100d04a26",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DesertRuins.Name",
    display_name="Desert Ruins",
    searchable_by=["Desert Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=88,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Desert Ruins",
        trigger=Triggers.BETWEEN_TURNS,
        effect=stadium_checkup_counters(1, pokemon_is_ex_with_hp(100), own_side_only=True),
    ),
)
