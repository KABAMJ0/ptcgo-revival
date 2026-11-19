from ptcgo.game.data_utils import StadiumCardDef, unimplemented, def_for
from ptcgo.game.card_effects.passives_common import ability_lock_passive
from ptcgo.game.attributes import Rarities

def is_basic_pokemon_def(pokemon) -> bool:
    """Silent Lab names Basic Pokemon; the stage is on the definition."""
    definition = def_for(getattr(pokemon, "archetype_id", "") or "")
    return getattr(definition, "stage", None) is not None \
        and int(getattr(definition.stage, "value", definition.stage)) == 0


card = StadiumCardDef(
    guid="ff59974c-334d-58fb-bd26-96f35695006e",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SilentLab.Name",
    display_name="Silent Lab",
    searchable_by=["Silent Lab", "Stadium"],
    subtypes=["Stadium"],
    collector_number=140,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=ability_lock_passive(lambda p, c: is_basic_pokemon_def(p))
)
