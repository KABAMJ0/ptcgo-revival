from ptcgo.game.data_utils import StadiumCardDef, def_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.passives import Passive

def _printed_name(pokemon) -> str:
    definition = def_for(getattr(pokemon, "archetype_id", None))
    printed = getattr(definition, "display_name", "") or ""
    return "".join(ch for ch in printed.lower() if ch.isalnum())


class _StarmieGymBoost(Passive):
    """Starmie-GX, on either side, does 40 more to the opponent's Active before
    Weakness and Resistance."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        attacker = calc.attacker
        if attacker is None or _printed_name(attacker) != "starmiegx":
            return
        if not calc.to_active:
            return
        calc.amount += 40

card = StadiumCardDef(
    guid="b418c08c-3243-5178-9945-39d37e5730f1",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysCeruleanCityGym.Name",
    display_name="Misty's Cerulean City Gym",
    searchable_by=["Misty's Cerulean City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=61,
    set_code="HF",
    rarity=Rarities.Uncommon,
    passive=_StarmieGymBoost(),
)
