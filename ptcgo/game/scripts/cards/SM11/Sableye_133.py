from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Triggers
from ptcgo.game.attributes import AttrID


async def shell_trap(ctx):
    """30. During the opponent's next turn, being damaged by an attack puts
    8 damage counters on the attacker (even if this Pokemon is KO'd)."""
    await ctx.deal_damage()
    ctx.attacker._shell_trap_until = ctx.session.turn_state.turn_number + 1
    entries = list(ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or [])
    if all(e.get("abilityID") != SHELL_TRAP_GRANTED.ability_id
           for e in entries if isinstance(e, dict)):
        entries.append(SHELL_TRAP_GRANTED.to_dict())
        await ctx.session._broadcast_entity_attribute(
            ctx.attacker, AttrID.PIE_ABILITIES, entries
        )


async def _shell_trap_trigger(ctx):
    """Fires on ON_DAMAGED_BY_ATTACK (put counters if still within the window)
    and on BETWEEN_TURNS (cleans up the grant once the window has passed)."""
    pokemon = ctx.source
    until = getattr(pokemon, "_shell_trap_until", None)
    if ctx.damaged_by is not None:
        if until is not None and ctx.session.turn_state.turn_number == until:
            await ctx.deal_damage(
                80, target=ctx.damaged_by, apply_modifiers=False, as_counters=True
            )
        return
    if until is not None and ctx.session.turn_state.turn_number >= until:
        pokemon._shell_trap_until = None
        entries = [
            e for e in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or [])
            if not (isinstance(e, dict) and e.get("abilityID") == SHELL_TRAP_GRANTED.ability_id)
        ]
        await ctx.session._broadcast_entity_attribute(pokemon, AttrID.PIE_ABILITIES, entries)


SHELL_TRAP_GRANTED = Ability(
    title="Shell Trap",
    game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if it is Knocked Out), put 8 damage counters on the Attacking Pokémon.",
    trigger=(Triggers.ON_DAMAGED_BY_ATTACK, Triggers.BETWEEN_TURNS),
    effect=_shell_trap_trigger,
)


card = PokemonCardDef(
    guid="94173933-06b5-53d5-9965-d35904c34537",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=133,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=302,
    abilities=[
        Attack(
            title="Mirror Gem",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if it is Knocked Out), put 8 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=shell_trap,
        ),
    ],
)