from ptcgo.game.data_utils import StadiumCardDef, def_for
from ptcgo.game.attributes import Rarities, AttrID, CardType
from ptcgo.game.card_effects.trainers import stadium_no_weakness


def _holds_plasma_energy(pokemon):
    """Predicate: an Energy card named Plasma Energy is attached to `pokemon`."""
    stack = list(pokemon.children)
    while stack:
        entity = stack.pop()
        stack.extend(getattr(entity, "children", []) or [])
        if entity.get_attribute(AttrID.CARD_TYPE) != CardType.ENERGY.value:
            continue
        definition = def_for(entity.archetype_id)
        if "plasma energy" in (getattr(definition, "display_name", "") or "").lower():
            return True
    return False

card = StadiumCardDef(
    guid="892bd555-cbe9-5221-b731-11585b08773b",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlasmaFrigate.Name",
    display_name="Plasma Frigate",
    searchable_by=["Plasma Frigate", "Stadium", "Team Plasma"],
    subtypes=["Stadium", "Team Plasma"],
    collector_number=124,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    passive=stadium_no_weakness(_holds_plasma_energy)
)
