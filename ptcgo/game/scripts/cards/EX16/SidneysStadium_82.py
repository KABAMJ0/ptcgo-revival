from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities, SpecialConditions
from ptcgo.game.card_effects.trainers import pokemon_of
from ptcgo.game.card_effects.passives_common import condition_immunity_passive


_DARKNESS = pokemon_of("darkness")


def _darkness_side(target, carrier):
    """(target, carrier) pred for the stadium passive: a Darkness Pokemon."""
    return _DARKNESS(target)


card = StadiumCardDef(
    guid="755abe03-b6d9-5bf6-b528-7d69d32a5e04",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SidneysStadium.Name",
    display_name="Sidney's Stadium",
    searchable_by=["Sidney's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=82,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    passive=condition_immunity_passive(
        (SpecialConditions.ASLEEP, SpecialConditions.CONFUSED,
         SpecialConditions.PARALYZED),
        protects=_darkness_side),
)
