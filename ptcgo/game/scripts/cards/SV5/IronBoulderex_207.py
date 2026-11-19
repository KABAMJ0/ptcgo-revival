from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
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
    guid="bb5d8b83-97c3-5d10-85da-584ccfc5e812",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBoulderex.Name",
    display_name="Iron Boulder ex",
    searchable_by=["Iron Boulder ex", "Basic", "ex", "Future", "IronBoulderex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=207,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    abilities=[
        Attack(
            title="Repulsor Axe",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if it is Knocked Out), put 8 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=shell_trap,
        ),
        Attack(
            title="Power Stomp",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)