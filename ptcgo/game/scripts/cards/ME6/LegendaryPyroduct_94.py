from ptcgo.game.data_utils import StadiumCardDef, unimplemented, def_for
from ptcgo.game.card_effects.passives_common import ability_lock_passive
from ptcgo.game.attributes import Rarities

def _stage_of(pokemon) -> int:
    definition = def_for(getattr(pokemon, "archetype_id", "") or "")
    stage = getattr(definition, "stage", None)
    return int(getattr(stage, "value", stage)) if stage is not None else -1


card = StadiumCardDef(
    guid="f892c948-6533-566f-bafb-3c301c0b5dad",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LegendaryPyroduct.Name",
    display_name="Legendary Pyroduct",
    searchable_by=["Legendary Pyroduct", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    passive=ability_lock_passive(lambda p, c: _stage_of(p) >= 1)
)
