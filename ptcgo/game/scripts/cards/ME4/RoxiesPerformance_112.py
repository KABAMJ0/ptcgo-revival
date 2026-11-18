from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import (
    AttrID, Rarities, SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES,
)
from ptcgo.game.card_effects.passives_common import no_retreat_passive, opposing_pokemon

_POISONED = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]


async def roxies_performance(ctx):
    """During your opponent's next turn, their Poisoned Pokemon can't retreat.
    (This includes newly Poisoned Pokemon.) The predicate is read live at every
    retreat check, so a Pokemon Poisoned after this resolves is covered too."""
    lock = no_retreat_passive(
        lambda p, c: opposing_pokemon(p, c)
        and _POISONED in (p.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    )
    for pokemon in ctx.my_pokemon_in_play():
        ctx.add_passive_through_opponents_turn(pokemon, lock)


card = SupporterCardDef(
    guid="9b855166-7f69-52e5-aaae-cd6a1d5b81ba",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoxiesPerformance.Name",
    display_name="Roxie's Performance",
    searchable_by=["Roxie's Performance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="ME4",
    rarity=Rarities.Rare,
    effect=roxies_performance
)
