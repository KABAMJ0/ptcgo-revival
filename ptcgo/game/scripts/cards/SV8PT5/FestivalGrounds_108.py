from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import condition_immunity_passive
from ptcgo.game.models.board import EnergyEntity


def _has_energy(pokemon):
    stack = list(pokemon.children)
    while stack:
        entity = stack.pop()
        if isinstance(entity, EnergyEntity):
            return True
        stack.extend(entity.children)
    return False


def _energy_holder(target, carrier):
    """(target, carrier) pred for the stadium passive: has any Energy attached."""
    return _has_energy(target)


async def _festival_grounds(ctx):
    """Clear the Special Conditions already on every Pokemon with Energy."""
    for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        if _has_energy(pokemon):
            await ctx.cure_all_conditions(pokemon)


async def _festival_grounds_attach(ctx):
    """A Pokemon that just gained Energy recovers from what it already had."""
    receiver = ctx.energy_receiver
    if receiver is not None and _has_energy(receiver):
        await ctx.cure_all_conditions(receiver)


card = StadiumCardDef(
    guid="227ea10d-98af-51af-90d0-7656dd3cd584",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FestivalGrounds.Name",
    display_name="Festival Grounds",
    searchable_by=["Festival Grounds", "Stadium"],
    subtypes=["Stadium"],
    collector_number=108,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    passive=condition_immunity_passive(protects=_energy_holder),
    effect=_festival_grounds,
    abilities=[
        Ability(
            title="Festival Grounds",
            game_text="Each Pok\u00e9mon that has any Energy attached (both "
                      "yours and your opponent's) recovers from all Special "
                      "Conditions and can't be affected by any Special "
                      "Conditions.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_festival_grounds_attach,
        ),
    ],
)
