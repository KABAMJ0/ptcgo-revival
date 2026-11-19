from ptcgo.game.data_utils import ItemCardDef, subtypes_for
from ptcgo.game.attributes import AttrID, Rarities
from ptcgo.game.models.board import PokemonEntity
from ptcgo.game.card_effects.trainers import pokemon_of
from ptcgo.game.session.passives import Passive

class _CannotEvolveThisTurn(Passive):
    """(That Pokemon can't evolve this turn.) -- effect-scoped evolution lock."""

    def blocks_evolution(self, player_id, target, carrier):
        return True


def _evolved(pokemon):
    return any(stage in ("Stage 1", "Stage 2", "VMAX", "BREAK")
               for stage in subtypes_for(pokemon.archetype_id))


def _previous_stage(pokemon):
    """The Evolution card tucked under `pokemon` that becomes the new top."""
    evolves_from = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)
    return next((child for child in pokemon.children
                 if isinstance(child, PokemonEntity)
                 and child.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == evolves_from),
                None)


async def _timepiece(ctx):
    """Put any number of Evolution cards from 1 evolved Psychic Pokemon into
    the hand; the Pokemon left in play cannot evolve this turn."""
    pool = [p for p in ctx.my_pokemon_in_play()
            if pokemon_of("psychic")(p) and _evolved(p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose an evolved Psychic Pokemon")
    if target is None:
        return
    stage = target
    while _evolved(stage):
        previous = _previous_stage(stage)
        if previous is None:
            break
        if not await ctx.ask_yes_no(
                "Put another Evolution card into your hand?"):
            break
        if not await ctx.devolve_pokemon(stage, 1, "hand"):
            break
        stage = previous
    ctx.add_temporary_passive(
        stage, _CannotEvolveThisTurn(),
        expires_after_turn=ctx.session.turn_state.turn_number)


card = ItemCardDef(
    guid="a9fda174-92be-5c3a-81c7-ce7eb789ea19",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrangeTimepiece.Name",
    display_name="Strange Timepiece",
    searchable_by=["Strange Timepiece", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    effect=_timepiece,
)
