from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import (
    is_in_active_spot, prevent_damage_when,
)
from ptcgo.game.session.passives import carrier_pokemon


def _holder_on_bench(calc, carrier):
    holder = carrier_pokemon(carrier)
    return (holder is not None and calc.target is holder
            and not is_in_active_spot(holder))


card = PokemonToolCardDef(
    guid="853c3710-b026-5148-bbc5-eb4bdf9d7fa7",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BenchShield.Name",
    display_name="Bench Shield",
    searchable_by=["Bench Shield", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=83,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    passive=prevent_damage_when(_holder_on_bench, attacks_only=True,
                                any_side=True)
)
