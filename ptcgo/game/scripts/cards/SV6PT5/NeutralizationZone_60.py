from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import prevent_damage_when
from ptcgo.game.card_effects.trainers import (
    is_pokemon_ex, is_pokemon_v_card, is_rule_box_pokemon,
)


def _no_rule_box_target(calc, carrier):
    """An opposing Pokemon ex or Pokemon V attacking a Pokemon with no Rule Box."""
    return (
        calc.is_opposing
        and not is_rule_box_pokemon(calc.target)
        and (is_pokemon_ex(calc.attacker) or is_pokemon_v_card(calc.attacker))
    )

card = StadiumCardDef(
    guid="17ac267d-07d9-538e-8786-3510d0c7c2ce",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NeutralizationZone.Name",
    display_name="Neutralization Zone",
    searchable_by=["Neutralization Zone", "Stadium", "ACE SPEC"],
    subtypes=["Stadium", "ACE SPEC"],
    collector_number=60,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    passive=prevent_damage_when(_no_rule_box_target),
)
